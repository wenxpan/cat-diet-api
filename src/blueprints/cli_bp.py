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
                 'johnisuser123').decode('utf-8')),
        User(username='Frank',
             email='frank@gmail.com',
             password=bcrypt.generate_password_hash(
                 'frankisuser123').decode('utf-8'))
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
            year_adopted='2021', breed='Domestic Shorthair',
            owner_id=1),
        Cat(name='Leo', year_adopted='2022',
            breed='Exotic Shorthair',
            owner_id=2),
        Cat(name='Milo', year_born='2015',
            year_adopted='2019', breed='Ragdoll',
            owner_id=2),
        Cat(name='Oreo', year_adopted='2019',
            breed='Domestic Longhair',
            owner_id=3),
    ]

    db.session.query(Cat).delete()
    db.session.add_all(cats)
    db.session.commit()

    # seed notes
    notes = [
        Note(cat_id=1, food_id=1, message='my cat likes it'),
        Note(cat_id=2, food_id=1, message='my cat likes it'),
        Note(cat_id=2, food_id=2, message='my cat hates it', is_negative=True),
        Note(cat_id=3, food_id=3, message='ate half the portion'),
        Note(cat_id=4, food_id=3, message='sniffed and went away', is_negative=True)
    ]
    db.session.query(Note).delete()
    db.session.add_all(notes)
    db.session.commit()

    print('Models seeded')
