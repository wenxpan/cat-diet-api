from flask import Blueprint
from init import db, bcrypt
from models.user import User, UserSchema
from utils.analyse import get_user_statistics
from flask_jwt_extended import jwt_required
from utils.authorise import admin_required, admin_or_owner_required
from flask import request
from sqlalchemy.exc import IntegrityError

# create blueprint for the /users endpoint
users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/')
@jwt_required()
def all_users():
    # returns a list of users

    # admin access only
    admin_required()

    # build query: select all users from users table
    stmt = db.select(User)
    # execute query and return scalars result
    users = db.session.scalars(stmt)

    # return serialized result, exclude sensitive info
    return UserSchema(many=True, exclude=['password']).dump(users)


@users_bp.route('/', methods=['POST'])
@jwt_required()
def create_user():
    # allows admin to create a user or admin in the database

    # admin access only
    admin_required()
    try:
        # load data using schema to sanitize and validate input
        user_info = UserSchema().load(request.json)

        # create a new User model instance, hash the password using bcrypt
        user = User(
            username=user_info['username'],
            email=user_info['email'],
            password=bcrypt.generate_password_hash(
                user_info['password']).decode('utf-8'),
            is_admin=user_info['is_admin']
        )

        # add and commit user to db
        db.session.add(user)
        db.session.commit()

        # return serialized user instance, exclude sensitive info (password)
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        # if email address is not unique, return error
        return {'error': 'Email already in use'}, 409


@users_bp.route('/<int:user_id>')
@jwt_required()
def get_one_user(user_id):
    # returns information and statistics of the selected user

    # build query: select user with matching id
    stmt = db.select(User).filter_by(id=user_id)
    # execute query and return a scalar result
    user = db.session.scalar(stmt)
    if user:
        # check if the user with token is admin or accessing their own profile
        admin_or_owner_required(user.id)

        # convert user object to JSON format
        user_info = UserSchema(exclude=['password']).dump(user)
        # add user statistics to JSON result
        user_info['statistics']=get_user_statistics(user_id)
        return user_info
    else:
        # if no user retrieved from db, return error
        return {'error': 'User not found'}, 404


@users_bp.route('/<int:user_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(user_id):
    # allows admin or owner to update user information of the selected id 
    # admin status cannot be updated for consistency and security reasons

        # build query: select user with matching id
        stmt = db.select(User).filter_by(id=user_id)
        # execute query and return a scalar result
        user = db.session.scalar(stmt)

        if user:
            # check if the user with token is admin or accessing their own profile
            admin_or_owner_required(user.id)
            try:
                # load data using schema to sanitize and validate input
                user_info = UserSchema().load(request.json, partial=True)

                # all fields can be optional, so get methods are used
                user.username = user_info.get('username', user.username)
                user.email = user_info.get('email', user.email)

                # check if input includes password; if yes, hash the password
                new_password = user_info.get('password')
                user.password = bcrypt.generate_password_hash(
                    new_password).decode('utf-8') if new_password else user.password
                
                # commit changes to db
                db.session.commit()

                # return updated user
                return UserSchema(exclude=['password', 'cats']).dump(user)
            except IntegrityError:
                # if unique constraint breached for email, return error
                return {'error': 'Email address is already used by other accounts'}, 409
        else:
            # if no user retrieved from db, return error
            return {'error': 'User not found'}, 404


@users_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    # allows admin to delete a user from database
    
    # admin access only
    admin_required()

    # build query: select user with matching id
    stmt = db.select(User).filter_by(id=user_id)
    # execute query and return a scalar result
    user = db.session.scalar(stmt)

    if user:
        # delete user instance and commit changes to db
        db.session.delete(user)
        db.session.commit()

        # return success message
        return {'message': f"User {user_id} and related cats and notes deleted"}, 200
    else:
        # if no user is retrived from db, return error
        return {'error': 'User not found'}, 404
