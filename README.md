# T2A2

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

## Problem identification (R1)

## Problem justification (R2)

Scenarios:

- when your cat is on diet, need to keep track of the treats
- check which one is the cat's favourite food, least favourite food

## Database system: benefits and drawbacks (R3)

## Functionalities and benefits of an ORM (R4)

## API endpoints (R5)

Here is an overview of the API endpoints:
![endpoints-overview](docs/endpoints-overview.png)

Visit links below to see full documentation:

- [API documentation - Postman version](https://documenter.getpostman.com/view/28027782/2s93zB5MTY#intro)
- [API documentation - Markdown version](/docs/endpoints.md)

## ERD (R6)

![ERD for Cat Diet API](./docs/erd.png)

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

### User Model

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

## Database relations (R9)

<!-- R9 (database terminology) - at the lower level, the same relationships at the database level; tables, foreign key, primary key, use database language to talk about how it works, how the relationships work -->

## Project planning and implementation (R10)

- [Trello Board](https://trello.com/b/IJJ0hY8f/t2a2-implementation-plan)
