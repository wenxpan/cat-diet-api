from flask import Blueprint
from init import db, bcrypt
from flask import request
from models.user import User, UserSchema
from utils.analyse import get_user_statistics
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from datetime import timedelta


# create blueprint for the /auth endpoint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('register', methods=['POST'])
def register():
    # creates a user in the database

    try:
        # load and sanitize data using marshmallow schema
        user_info = UserSchema().load(request.json)

        # create a new User model instance, hash the password using bcrypt
        user = User(username=user_info['username'],
                    email=user_info['email'],
                    password=bcrypt.generate_password_hash(
            user_info['password']).decode('utf-8'))

        # add and commit user to db
        db.session.add(user)
        db.session.commit()

        # return serialized user instance, exclude sensitive info (password)
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        # if email address is not unique, return error
        return {'error': 'Email already in use'}, 409


@auth_bp.route('login', methods=['POST'])
def login():
    # allows user to login and receive a token for authentication and authorization

    try:
        # build query: select the user with matching email
        stmt = db.select(User).filter_by(email=request.json['email'])
        # execute query and return a scalar result
        user = db.session.scalar(stmt)

        # hash input password and check against the hashed string in db
        if user and bcrypt.check_password_hash(user.password, request.json['password']):
            # if passwords match, create access token with the user's id as identity
            # set token expiry as 1 day
            token = create_access_token(
                identity=user.id, expires_delta=timedelta(days=1))
            # return generated token, user information and statistics summary
            return {'token': token,
                    'user': UserSchema(exclude=['password', 'cats']).dump(user),
                    'statistics': get_user_statistics(user.id)}
        # if user not in db or passwords do not match, return error
        else:
            return {'error': 'Invalid email or password'}, 401
    # if either email or password not provided, return error
    except KeyError:
        return {'error': 'Email and password are required'}, 400