from flask_jwt_extended import get_jwt_identity
from flask import abort
from init import db
from models.user import User

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
