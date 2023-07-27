# Cat Diet API

The REST API aims to assist cat owners in tracking and managing their cat's diet and food preferences, as well as monitoring any changes over time, in order to keep a well-balanced diet for their cats.

## API Documentation

- [Cat Diet API - Postman](https://documenter.getpostman.com/view/28027782/2s93zB5MTY)

## Installation and setup

1. Open terminal and run the PostgreSQL prompt:

   ```
   psql
   ```

2. Create and connect to database:

   ```
   Create DATABASE cat_diet;
   \c cat_diet;
   ```

3. Create a user with password and grant user priviliges:

   ```
   CREATE USER cat_diet_dev WITH PASSWORD 'admin123';
   GRANT ALL PRIVILEGES ON DATABASE cat_diet TO cat_diet_dev;
   ```

4. Open another terminal. Use `cd` command and direct to the `WenxuanPan_T2A2/src` directory

5. Create and activate virtual environment:

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

6. Install dependencies

   ```
   python3 -m pip install -r requirements.txt
   ```

7. Rename `.env.sample` to `.env`, and set the db connection string and JWT secret key:

   ```
   DB_URI=postgresql+psycopg2://cat_diet_dev:admin123@localhost:5432/cat_diet
   JWT_KEY=Your Secret Key
   ```

8. In terminal, create and seed the database, then run the flask app:

   ```
   flask db create
   flask db seed
   flask run
   ```

The server will run on `http://127.0.0.1:5000`.

## ERD

![ERD for Cat Diet API](./docs/erd.png)

## Tech stack

The REST API was built using Flask, with the following third-party services (for full list, see [src/requirements.txt](/src/requirements.txt)):

### SQLAlchemy (2.0.16) & Flask-SQLAlchemy (3.0.3)

SQLAlchemy is an ORM tool that serves as a bridge between python and the database (postgreSQL). In this project, it is used together with its wrapper Flask-SQLAlchemy to define models that represent database tables using python classes as well as translating python codes into SQL queries, achieving an object-oriented approach to data manipulation and makes the code easier to maintain.

### psycopg2 (2.9.6)

Psycopg is the [PostgreSQL database adapter](https://pypi.org/project/psycopg2/) for Python. It is specified in the DB_URI connection string, e.g. `DB_URI="postgresql+psycopg2://dev:password@localhost:5432/db"`, in order to assist SQLAlchemy to interact with PostgreSQL.

### marshmallow (3.19.0) & Flask-marshmallow (0.15.0)

Marshmallow is an ORM library used to:

- convert app-level objects to JSON format using `Schema.dump()`
- load input data to app-level objects using `Schema.load()`
  - raise `ValidationError` when input data doesn't meet validation requirements

### Flask-Bcrypt (1.0.1)

Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for application. It is designed to be ["de-optimized"](https://pypi.org/project/Flask-Bcrypt/) so that hashed data is more difficult to crack than other faster algorithms.

In this project, it is used to hash user passwords before storing it to db and verify passwords during login. By doing so, it adds an additional security layer and ensures that sensitive data is safely handled and will not expose to anyone.

### python-dotenv (1.0.0)

Python-dotenv is used to read key-value pairs from a .env file and can set them as environment variables.

In this project, `.env` file is created to store JWT secret key and SQLAlechemy's database connection string. The file is not published to remote repo, ensuring that confidential information is stored safely, and users can set their own environment variables on their end by setting up `.env` file.

### Flask-JWT-Extended (4.5.2)

Flask-JWT-Extended is used to integrate JWT (JSON Web Tokens) support in the flask app. This helps to ensure that user's identity is authenticated before they perform sensitive operations. For example, a person cannot create new food if they are not logged in (i.e. no token in the request header). It also helps maintaining authorisation levels. For example, a user cannot add notes for a cat that they don't own; this is verified by getting identity from the token and checking it against the owner id in the database.

## Project planning

For the timeline of this project, see [Trello Board](https://trello.com/b/IJJ0hY8f/t2a2-implementation-plan)
