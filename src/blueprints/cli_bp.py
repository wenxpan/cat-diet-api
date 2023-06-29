from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.food import Food
from models.ingredient import Ingredient
from models.cat import Cat
from models.note import Note

# create blueprint for the /auth endpoint
cli_bp = Blueprint('db', __name__)


@cli_bp.cli.command('create')
def create_db():
    # drop and create tables using 'flask db create'

    db.drop_all()
    db.create_all()
    print('Tables created successfully')


@cli_bp.cli.command('seed')
def seed_db():
    # seed tables using 'flask db seed'

    # seed user
    users = [
        User(username='MaryDev',
             email='marydev@gmail.com',
             password=bcrypt.generate_password_hash(
                 'maryisadmin123').decode('utf-8'), 
                is_admin=True, 
                joined_since='2023-06-20'), 
        User(username='John',
             email='john@gmail.com',
             password=bcrypt.generate_password_hash(
                 'johnisuser123').decode('utf-8'), 
                 joined_since='2023-06-20'),
        User(username='Frank',
             email='frank@gmail.com',
             password=bcrypt.generate_password_hash(
                 'frankisuser123').decode('utf-8'),
                 joined_since='2023-06-20')
    ]
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

    # seed ingredients
    ingredients = [
        Ingredient(name='Chicken', category='Meat'),
        Ingredient(name='Lamb', category='Meat'),
        Ingredient(name='Brown Rice', category='Grains'),
        Ingredient(name='Ground Wheat', category='Grains'),
        Ingredient(name='Tuna', category='Seafood'),
        Ingredient(name='Prawn', category='Seafood'),
        Ingredient(name='Chicken Meal', category='Derivatives')
        ]

    db.session.query(Ingredient).delete()
    db.session.add_all(ingredients)
    db.session.commit()

    # seed food
    food = [
        Food(category='Wet', name='Tuna With Prawn Canned Adult Cat Food',
             brand='Applaws', ingredients=[ingredients[4], ingredients[5]]),
        Food(category='Wet', name='Chicken Wet Cat Food Cans', 
             brand='Ziwi', ingredients=[ingredients[0]]),
        Food(category='Dry', name='Adult Oral Care Dry Cat Food',
             brand='Hills Science Diet', ingredients=[ingredients[0], ingredients[2]]),
        Food(category='Treats', name='Feline Treats Dental Catnip Flavour Tub',
             brand='Greenies', ingredients=[ingredients[6], ingredients[3]])
    ]

    db.session.query(Food).delete()
    db.session.add_all(food)
    db.session.commit()

    # seed cats
    cats = [
        Cat(name='Luna', year_born='2020',
            year_adopted='2021', breed='Domestic Shorthair',
            owner=users[1]),
        Cat(name='Leo', year_adopted='2022',
            breed='Exotic Shorthair',
            owner=users[2]),
        Cat(name='Milo', year_born='2015',
            year_adopted='2019', breed='Ragdoll',
            owner=users[2]),
        Cat(name='Oreo', year_adopted='2019',
            breed='Domestic Longhair',
            owner=users[2])
    ]

    db.session.query(Cat).delete()
    db.session.add_all(cats)
    db.session.commit()

    # seed notes
    notes = [
        Note(cat=cats[0], food=food[0], rating=0, message=
             'Luna was ok with it, maybe will try a different one', 
             date_recorded='2023-06-24'),
        Note(cat=cats[0], food=food[3], rating=1, message=
             'Luna likes the treats', date_recorded='2023-06-24'),
        Note(cat=cats[0], food=food[1], rating=0, message=
             'Tried a different can and Luna only ate half of it', 
             date_recorded='2023-06-25'),
        Note(cat=cats[0], food=food[1], rating=1, message=
             'Luna ate the whole can, she likes it!', 
             date_recorded='2023-06-26'),
        Note(cat=cats[0], food=food[1], rating=1, message=
             'Luna is still happy with it!', 
             date_recorded='2023-06-26'),
        Note(cat=cats[1], food=food[1], rating=-1, message=
             'Leo hates it', date_recorded='2023-06-20'),
        Note(cat=cats[2], food=food[1], rating=0, message=
             'Milo was the only cat eating the can, but not finished it either', 
             date_recorded='2023-06-20'),
        Note(cat=cats[3], food=food[1], rating=-1, message=
             'Oreo sniffed and went away', date_recorded='2023-06-20'),
        Note(cat=cats[1], food=food[3], rating=1, message=
             'Leo likes it', date_recorded='2023-06-21'),
    ]
    db.session.query(Note).delete()
    db.session.add_all(notes)
    db.session.commit()

    print('Models seeded')
