# T2A2 - Cat Diet API

## Links

- [Github repo](https://github.com/wenxuan-pan/WenxuanPan_T2A2)
- [Trello Board](https://trello.com/b/IJJ0hY8f/t2a2-implementation-plan)
- [API Documentation](https://documenter.getpostman.com/view/28027782/2s93zB5MTY)

## Installation and setup

- Open terminal and run the PostgreSQL prompt:

```
psql
```

- Create and connect to database

```
Create DATABASE cat_diet;
\c cat_diet;
```

- Create a user with password and grant user priviliges:

```
CREATE USER cat_diet_dev WITH PASSWORD 'admin123';
GRANT ALL PRIVILEGES ON DATABASE cat_diet TO cat_diet_dev;
```

- Open another terminal. Use `cd` command and direct to the `WenxuanPan_T2A2/src` directory

- Create and activate virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

- Install dependencies

```
python3 -m pip install -r requirements.txt
```

- Rename `.env.sample` to `env`, and set the db connection string and JWT secret key:

```
DATABASE_URL=postgresql+psycopg2://cat_diet_dev:admin123@localhost:5432/cat_diet
JWT_SECRET_KEY=Your Secret Key
```

- In terminal, create and seed the database, then run the flask app:

```
flask db create
flask db seed
flask run
```

The server will run on `http://127.0.0.1:5000`.

## Problem identification and justification (R1/R2)

The REST Cat Diet API aims to assist cat owners in tracking and managing their cat's diet and food preferences, as well as monitoring any changes over time, in order to keep a well-balanced diet for their cats.

In particular, the app addresses the following issues:

### Fussy eating

Many cats are known to be picky eaters, and it can be challenging for cat owners to identify their cat's favourite and least favourite foods. The app provides a centralised platform for cat owners to record and track their cat's preferences, making it easier for them to choose suitable food options.

### Health and nutrition

The [Code of Practice for the Private Keeping of Cats](https://agriculture.vic.gov.au/livestock-and-animals/animal-welfare-victoria/domestic-animals-act/codes-of-practice/code-of-practice-for-the-private-keeping-of-cats#h2-6) sets the following minimum standards regarding nutrition:

> Cats must be fed a diet that provides proper and sufficient food to maintain good health and meet their physiological needs.
>
> Cats are carnivores and must not be fed a purely vegetarian diet.
>
> Cats must not be fed a diet consisting purely of fresh meat (including fish).

To meet these standards, owners can use this app to regularly monitor the food type and ingredients to ensure that their cat receives the necessary nutrients and avoid potential health issues caused by an imbalanced diet.

### Avoiding overfeeding treats

Treats are given as rewards for cats, but excessive consumption can lead to weight gain and health issues, and owners might not always realise that they are overfeeding. The app allows cat owners to keep track of treat consumption and review on a regular basis to prevent overfeeding.

### Identifying allergies or intolerances

Cats can have allergies or food intolerances, and it may take time for owners to realised and identify specific ingredients or brands that cause adverse reactions in their cats. The app allows users to note down their cat's any resistance or adverse reactions to certain foods or ingredients, which can be helpful during vet consultation and finding solutions. This will also help cat owners remember and avoid purchasing similar products in the future.

## Database system: benefits and drawbacks (R3)

## Functionalities and benefits of an ORM (R4)

## API endpoints (R5)

Here is an overview of the API endpoints:
![endpoints-overview](docs/endpoints-overview.png)

Visit links below to see full documentation:

- [API documentation - Postman version](https://documenter.getpostman.com/view/28027782/2s93zB5MTY#intro)
- [API documentation - Markdown version](/docs/endpoints.md)

## ERD and database relations (R6/R9)

![ERD for Cat Diet API](./docs/erd.png)

<!-- R9 (database terminology) - at the lower level, the same relationships at the database level; tables, foreign key, primary key, use database language to talk about how it works, how the relationships work -->

## Third party services (R7)

### Flask (2.3.2)

The REST API was built using Flask, a Python micro-framework that runs on the server-side, providing essential functionalities to handle the incoming request, determine the route and request methods, and send an appropriate response back to the client.

The following third-party services are used in this app (for full list, see [src/requirements.txt](/src/requirements.txt)).

### SQLAlchemy (2.0.16)

SQLAlchemy is an Object Relational Mapper tool that serves as a bridge between python and the database (postgresql).

It is used for defining models and querying data.

Flask-SQLAlchemy (3.0.3)

![sqlalchemy in code](/docs/sqlalchemy-example.png)

### psycopg2 (2.9.6)

### Flask-marshmallow (0.15.0)

### Flask-Bcrypt (1.0.1)

### Flask-JWT-Extended (4.5.2)

### python-dotenv (1.0.0)

## Porject models and relationships (R8)

Describe your projects models in terms of the relationships they have with each other

<!-- R8 (python code) - about SQLAlchemy models, relationships between the models using sqlalchemy language; `db.relationship`, `db.ForeignKey` -->

There are 5 models created in this project: User, Cat, Food, Ingredient, Note. There is an additional join table food_ingredient that reflects the many-to-many relationship between Food and Ingredient.

### User model

```python
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    joined_since = db.Column(db.Date, default=date.today())

    cats = db.relationship('Cat', back_populates='owner',
                           cascade='all, delete')
```

- The primary key of the model is `id`, defined using `primary_key=True`.
- `username`, `email`, `password` and `is_admin` are set as `nullable=False`, meaning they are required fields. If no value of `is_admin` is given, it will be set as default False.
- Instead of `db.ForeignKey`, the User model just has a `db.relationship` with `cats`, representing the one-to-many relationship: one user can have many cats; and as it back populates with the single `owner` in `Cat` model, one cat can only belong to one owner. `cascade='all, delete'` means that the cats will be removed if their owner is deleted.

Returned JSON result:

```JSON
{
    "id": 2,
    "username": "John",
    "email": "john@gmail.com",
    "is_admin": false,
    "joined_since": "2023-06-20",
    "cats": [
        {
            "id": 1,
            "name": "Luna",
            "breed": "Domestic Shorthair",
            "year_born": 2020,
            "year_adopted": 2021
        }
    ]
}
```

The nested list of cats is created through marshmallow schema:

```python
cats = fields.List(fields.Nested('CatSchema', exclude=['owner_id', 'owner', 'notes']))
```

### Cat model

```python
class Cat(db.Model):
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year_born = db.Column(db.Integer)
    year_adopted = db.Column(db.Integer)
    breed = db.Column(db.String(100))

    owner_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    owner = db.relationship('User', back_populates='cats')

    notes = db.relationship(
        'Note', back_populates='cat', cascade='all, delete')
```

returned JSON result

```JSON
{
    "id": 1,
    "name": "Luna",
    "breed": "Domestic Shorthair",
    "year_born": 2020,
    "year_adopted": 2021,
    "owner": {
        "username": "John"
    },
    "notes": []
}
```

marshmallow schema

```python
owner = fields.Nested('UserSchema', only=[
                      'username'])
notes = fields.List(fields.Nested('NoteSchema', exclude=[
    'cat', 'cat_id', 'food_id']))
```

### Food model

```python
class Food(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    brand = db.Column(db.String(100))
    category = db.Column(db.String(30))

    ingredients = db.relationship(
        'Ingredient', secondary=food_ingredient, back_populates='foods')

    notes = db.relationship(
        'Note', back_populates='food', cascade='all, delete')
```

returned JSON result

```JSON
{
    "id": 1,
    "name": "Tuna With Prawn Canned Adult Cat Food",
    "brand": "Applaws",
    "category": "Wet",
    "ingredients": [
        {
            "id": 5,
            "name": "Tuna",
            "category": "Seafood"
        },
        {
            "id": 6,
            "name": "Prawn",
            "category": "Seafood"
        }
    ],
    "notes": []
}
```

marshmallow schema

```python
ingredients = fields.List(fields.Nested(
    'IngredientSchema', exclude=['foods']))
notes = fields.List(fields.Nested('NoteSchema', exclude=[
    'food_id', 'food', 'cat_id']))
```

### Ingredient model

```python
class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(30))

    foods = db.relationship(
        'Food', secondary=food_ingredient, back_populates='ingredients')
```

returned JSON result

```JSON
{
    "id": 1,
    "name": "Chicken",
    "category": "Meat",
    "foods": [
        {
            "id": 2,
            "name": "Chicken Wet Cat Food Cans",
            "brand": "Ziwi",
            "category": "Wet"
        }
    ]
}
```

marshmallow schema:

```python
foods = fields.List(fields.Nested(
    'FoodSchema', exclude=['notes', 'ingredients']))
```

#### food_ingredient join table

```python
food_ingredient = db.Table('food_ingredient',
                           db.Column('food_id', db.Integer,
                                     db.ForeignKey('foods.id', ondelete='CASCADE'), primary_key=True),
                           db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id', ondelete='CASCADE'), primary_key=True))
```

### Note model

```python
class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    rating = db.Column(db.Integer, default=0)
    date_recorded = db.Column(db.Date, default=date.today())

    cat_id = db.Column(db.Integer, db.ForeignKey(
        'cats.id', ondelete='CASCADE'), nullable=False)
    cat = db.relationship('Cat', back_populates='notes')

    food_id = db.Column(db.Integer, db.ForeignKey(
        'foods.id', ondelete='CASCADE'), nullable=False)
    food = db.relationship('Food', back_populates='notes')
```

returned JSON

```JSON
{
    "id": 1,
    "message": "Luna was ok with it, maybe will try a different one",
    "rating": 0,
    "date_recorded": "2023-06-24",
    "cat": {
        "id": 1,
        "name": "Luna",
        "breed": "Domestic Shorthair",
        "owner": {
            "username": "John"
        }
    },
    "food": {
        "id": 1,
        "name": "Tuna With Prawn Canned Adult Cat Food",
        "brand": "Applaws",
        "category": "Wet",
        "ingredients": [
            {
                "id": 5,
                "name": "Tuna",
                "category": "Seafood"
            },
            {
                "id": 6,
                "name": "Prawn",
                "category": "Seafood"
            }
        ]
    }
}
```

marshmallow schema

```python
    cat = fields.Nested('CatSchema', only=['id', 'name', 'breed', 'owner'])
    food = fields.Nested('FoodSchema', exclude=['notes'])
```

## Project planning and implementation (R10)

- [Trello Board](https://trello.com/b/IJJ0hY8f/t2a2-implementation-plan)
