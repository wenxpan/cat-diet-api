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



### Auth routes

### User routes

### Food routes

### Ingredient routes

### Cat routes

### Notes routes

## ERD (R6)

![ERD for Cat Diet API](./docs/erd.png)

## Third party services (R7)

```
bcrypt==4.0.1
blinker==1.6.2
click==8.1.3
Flask==2.3.2
Flask-Bcrypt==1.0.1
Flask-JWT-Extended==4.5.2
flask-marshmallow==0.15.0
Flask-SQLAlchemy==3.0.3
greenlet==2.0.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
marshmallow==3.19.0
marshmallow-sqlalchemy==0.29.0
packaging==23.1
psycopg2-binary==2.9.6
PyJWT==2.7.0
python-dotenv==1.0.0
SQLAlchemy==2.0.16
typing_extensions==4.6.3
Werkzeug==2.3.6
```

## Porject models and relationships (R8)

## Database relations (R9)

## Project planning and implementation (R10)
