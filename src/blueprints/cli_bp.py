from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.food import Food
from models.cat import Cat
from models.note import Note
from models.ingredient import Ingredient, food_ingredient

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

    # seed ingredients
    ingredients = [Ingredient(name='chicken', category='Meat'),
                   Ingredient(name='mackerel', category='Fish'),
                   Ingredient(name='lamb', category='Meat')]

    db.session.query(Ingredient).delete()
    db.session.add_all(ingredients)
    db.session.commit()

    # seed food
    food = [
        Food(food_type='Wet', name='Chicken Wet Cat Food Cans',
             brand='Ziwi', ingredients=[ingredients[0], ingredients[1]]),
        Food(food_type='Dry', name='Adult Oral Care Dry Cat Food',
             brand='Hills Science Diet', ingredients=[Ingredient(name='new', category='Meat')]),
        Food(food_type='Dry', name='Feline Treats Dental Catnip Flavour Tub',
             brand='Greenies')
    ]

    db.session.query(Food).delete()
    db.session.add_all(food)
    db.session.commit()

    # seed cats
    cats = [
        Cat(name='Luna', year_born='2020',
            year_adopted='2021', breed='Domestic Shorthair',
            owner=users[0]),
        Cat(name='Leo', year_adopted='2022',
            breed='Exotic Shorthair',
            owner=users[1]),
        Cat(name='Milo', year_born='2015',
            year_adopted='2019', breed='Ragdoll',
            owner=users[1]),
        Cat(name='Oreo', year_adopted='2019',
            breed='Domestic Longhair',
            owner=users[2]),
    ]

    db.session.query(Cat).delete()
    db.session.add_all(cats)
    db.session.commit()

    # seed notes
    notes = [
        Note(cat=cats[0], food=food[0], rating=1, message='my cat likes it'),
        Note(cat=cats[1], food=food[0], rating=1, message='my cat likes it'),
        Note(cat=cats[1], food=food[1],
             message='my cat hates it', rating=-1),
        Note(cat=cats[2], food=food[2], message='ate half the portion'),
        Note(cat=cats[3], food=food[2],
             message='sniffed and went away', rating=-1)
    ]
    db.session.query(Note).delete()
    db.session.add_all(notes)
    db.session.commit()

    print('Models seeded')
