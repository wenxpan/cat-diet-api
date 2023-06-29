from flask import Blueprint, abort
from init import db, bcrypt
from flask import request
from models.user import User, UserSchema
from utils.analyse import get_user_statistics
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity
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
        stmt = db.select(User).filter_by(email=request.json['email'])
        user = db.session.scalar(stmt)
        if user and bcrypt.check_password_hash(user.password, request.json['password']):
            token = create_access_token(
                identity=user.id, expires_delta=timedelta(days=30))
            # change expiration back to 1 day when submitting
            return {'token': token,
                    'user': UserSchema(exclude=['password', 'cats']).dump(user),
                    'statistics': get_user_statistics(user.id)}
        else:
            return {'error': 'Invalid email or password'}, 401
    except KeyError:
        return {'error': 'Email and password are required'}, 400


def admin_required():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin):
        abort(401, description="You must be an admin")


def admin_or_owner_required(owner_id):
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin or user_id == owner_id):
        abort(401, description="You must be an admin or owner")
