from flask import Blueprint
from init import db
from models.ingredient import Ingredient, IngredientSchema
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required
from flask import request
from sqlalchemy.exc import IntegrityError

ingredients_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients')


@ingredients_bp.route('/')
def all_ingredients():
    # returns a list of ingredients and related foods

    stmt = db.select(Ingredient)
    ingredient = db.session.scalars(stmt)
    return IngredientSchema(many=True).dump(ingredient)


@ingredients_bp.route('/', methods=['POST'])
@jwt_required()
def create_ingredient():
    # creates a new ingredient in the database

    try:
        ingredient_info = IngredientSchema().load(request.json)
        ingredient = Ingredient(
            name=ingredient_info['name'],
            category=ingredient_info['category']
        )
        db.session.add(ingredient)
        db.session.commit()
        return IngredientSchema(exclude=['food']).dump(ingredient), 201
    except IntegrityError:
        # maybe add a function to return the food id
        return {'error': 'Ingredient name already exists'}


@ingredients_bp.route('/<int:ingredient_id>')
def get_one_ingredient(ingredient_id):
    # returns ingredient of the selected id

    stmt = db.select(Ingredient).filter_by(id=ingredient_id)
    ingredient = db.session.scalar(stmt)
    if ingredient:
        return IngredientSchema().dump(ingredient)
    else:
        return {'error': 'Ingredient not found'}, 404


@ingredients_bp.route('/<int:ingredient_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(ingredient_id):
    # updates ingredient information of the selected id

    admin_required()
    stmt = db.select(Ingredient).filter_by(id=ingredient_id)
    ingredient = db.session.scalar(stmt)
    ingredient_info = IngredientSchema().load(request.json, partial=True)
    if ingredient:
        ingredient.name = ingredient_info.get('name', ingredient.name)
        ingredient.category = ingredient_info.get(
            'category', ingredient.category)
        db.session.commit()
        return IngredientSchema(exclude=['food']).dump(ingredient)
    else:
        return {'error': 'Ingredient not found'}, 404


@ingredients_bp.route('/<int:ingredient_id>', methods=['DELETE'])
@jwt_required()
def delete_ingredient(ingredient_id):
    # allows admin to delete an ingredient from database
    
    admin_required()
    stmt = db.select(Ingredient).filter_by(id=ingredient_id)
    ingredient = db.session.scalar(stmt)
    if ingredient:
        db.session.delete(ingredient)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Ingredient not found'}, 404
