from flask_jwt_extended import get_jwt_identity
from flask import abort
from init import db
from models.user import User

def admin_required():
    # for authorization: check if the user with token is admin

    # get user_id from JWT token 
    user_id = get_jwt_identity()

    # build query: select user with matching id
    stmt = db.select(User).filter_by(id=user_id)
    # execute query and return a scalar result
    user = db.session.scalar(stmt)

    # if user is not in db or is not admin, return error
    if not (user and user.is_admin):
        abort(401, description="You must be an admin")


def admin_or_owner_required(owner_id):
    # for authorization: check if the user with token is admin or owner

    # get user_id from JWT token 
    user_id = get_jwt_identity()

    # build query: select user with matching id
    stmt = db.select(User).filter_by(id=user_id)
    # execute query and return a scalar result
    user = db.session.scalar(stmt)

    # if user is not in db, or if the user is not admin or owner, return error
    if not (user and user.is_admin or user_id == owner_id):
        abort(401, description="You must be an admin or owner")
