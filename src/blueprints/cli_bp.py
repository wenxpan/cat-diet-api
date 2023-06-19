from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.food import Food
from models.cat import Cat
from models.note import Note

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

    # seed food
    food = [
        Food(type='Wet Food', name='Chicken Wet Cat Food Cans', brand='Ziwi'),
        Food(type='Dry Food', name='Adult Oral Care Dry Cat Food',
             brand='Hills Science Diet'),
        Food(type='Treats', name='Feline Treats Dental Catnip Flavour Tub',
             brand='Greenies')
    ]

    db.session.query(Food).delete()
    db.session.add_all(food)
    db.session.commit()

    # seed cats
    cats = [
        Cat(name='Luna', year_born='2020',
            year_adopted='2021', breed='Domestic Shorthair'),
        Cat(name='Simba', year_adopted='2022',
            breed='Exotic Shorthair'),
        Cat(name='Milo', year_born='2015',
            year_adopted='2019', breed='Ragdoll'),
        Cat(name='Oreo', year_adopted='2019',
            breed='Domestic Longhair'),
    ]

    db.session.query(Cat).delete()
    db.session.add_all(cats)
    db.session.commit()

    # seed notes
    notes = [
        Note(message='my cat likes it'),
        Note(message='my cat hates it', is_negative=True)
    ]
    db.session.query(Note).delete()
    db.session.add_all(notes)
    db.session.commit()

    print('Models seeded')
