from flask import Blueprint
from init import db, bcrypt
from flask import request
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('register', methods=['POST'])
def register():
    try:
        user_info = UserSchema().load(request.json)
        user = User(username=user_info['username'], email=user_info['email'],
                    password=bcrypt.generate_password_hash(
            user_info['password']).decode('utf-8'))

        db.session.add(user)
        db.session.commit()

        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email already in use'}, 409


@auth_bp.route('login', methods=['POST'])
def login():
    try:
        stmt = db.select(User).filter_by(email=request.json['email'])
        user = db.session.scalar(stmt)
        if user and bcrypt.check_password_hash(user.password, request.json['password']):
            token = create_access_token(
                identity=user.id, expires_delta=timedelta(days=1))
            return {'token': token, 'user': UserSchema(exclude=['id', 'password']).dump(user)}
        else:
            return {'error': 'Invalid email or password'}, 401
    except:
        return {'error': 'Email and password are required'}, 400
