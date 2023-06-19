from flask import Blueprint
from init import db, bcrypt
from models.user import User, UserSchema
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required
from flask import request
from sqlalchemy.exc import IntegrityError


users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/')
@jwt_required()
def all_users():
    admin_required()
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)


@users_bp.route('/', methods=['POST'])
@jwt_required()
def create_user():
    admin_required()
    try:
        user_info = UserSchema().load(request.json)
        user = User(
            username=user_info['username'],
            email=user_info['email'],
            password=bcrypt.generate_password_hash(
                user_info['password']).decode('utf-8'),
            is_admin=user_info['is_admin']
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email already in use'}, 409
