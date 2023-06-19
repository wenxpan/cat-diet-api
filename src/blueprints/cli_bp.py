from flask import Blueprint
from init import db, bcrypt
from models.user import User


cli_bp = Blueprint('db', __name__)


@cli_bp.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables created successfully')


@cli_bp.cli.command('seed')
def seed_db():
    # seed user

    users = [
        User(username='MaryDev',
             email='marydev@gmail.com',
             password=bcrypt.generate_password_hash(
                 'maryisadmin123').decode('utf-8'), is_admin=True),
        User(username='John',
             email='john@gmail.com',
             password=bcrypt.generate_password_hash(
                 'johnisuser123').decode('utf-8'))
    ]
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()
    print('Models seeded')
