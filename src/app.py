from flask import Flask
from os import environ
from init import db, ma, bcrypt, jwt
from marshmallow.exceptions import ValidationError
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp
from blueprints.users_bp import users_bp
from blueprints.foods_bp import foods_bp
from blueprints.cats_bp import cats_bp
from blueprints.notes_bp import notes_bp
from blueprints.ingredients_bp import ingredients_bp


def create_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.json.sort_keys = False

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)}, 400
    
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages}, 400

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401
    
    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(foods_bp)
    app.register_blueprint(cats_bp)
    app.register_blueprint(notes_bp)
    app.register_blueprint(ingredients_bp)

    return app
