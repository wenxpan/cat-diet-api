# T2A2

## Links

- [Github repo](https://github.com/wenxuan-pan/WenxuanPan_T2A2)
- [Trello Board](https://trello.com/b/IJJ0hY8f/t2a2-implementation-plan)

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
