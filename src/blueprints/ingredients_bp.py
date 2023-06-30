from flask import Blueprint, request
from init import db
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
from models.ingredient import Ingredient, IngredientSchema
from utils.authorise import admin_required

# create blueprint for the /foods endpoint
ingredients_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients')


@ingredients_bp.route('/')
def all_ingredients():
    # returns a list of ingredients and related foods

    # build query: select all ingredients from ingredients table
    stmt = db.select(Ingredient)
    # execute query and return scalars result
    ingredient = db.session.scalars(stmt)

    # return serialized result
    return IngredientSchema(many=True).dump(ingredient)


@ingredients_bp.route('/', methods=['POST'])
@jwt_required()
def create_ingredient():
    # creates a new ingredient in the database

    try:
        # load data using schema to sanitize and validate input
        ingredient_info = IngredientSchema().load(request.json)

        # create a new Ingredient model instance
        ingredient = Ingredient(
            name=ingredient_info['name'],
            category=ingredient_info.get('category') # optional
        )

        # add and commit ingredient to db
        db.session.add(ingredient)
        db.session.commit()

        # return serialized result
        return IngredientSchema(exclude=['foods']).dump(ingredient), 201
    except IntegrityError:
        # if ingredient name is not unique, return error
        return {'error': 'Ingredient name already exists'}


@ingredients_bp.route('/<int:ingredient_id>')
def get_one_ingredient(ingredient_id):
    # returns ingredient of the selected id

    # build query: slect ingredient with matching id
    stmt = db.select(Ingredient).filter_by(id=ingredient_id)
    # execute query and return a scalar result
    ingredient = db.session.scalar(stmt)
    if ingredient:
        # return seraialized result
        return IngredientSchema().dump(ingredient)
    else:
        # if no ingredient is retrieved from db, return error
        return {'error': 'Ingredient not found'}, 404


@ingredients_bp.route('/<int:ingredient_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_ingredient(ingredient_id):
    # updates ingredient information of the selected id

    # admin access only
    admin_required()

    # build query: select ingredient with matching id
    stmt = db.select(Ingredient).filter_by(id=ingredient_id)
    # execute query and return a scalar result
    ingredient = db.session.scalar(stmt)

    if ingredient:
        # load data using schema to sanitize and validate input
        ingredient_info = IngredientSchema().load(request.json, partial=True)
        
        # update fields; all fields can be optional, so get methods are used
        ingredient.name = ingredient_info.get('name', ingredient.name)
        ingredient.category = ingredient_info.get(
            'category', ingredient.category)
        
        # commit changes to db
        db.session.commit()

        # return updated ingredients
        return IngredientSchema(exclude=['foods']).dump(ingredient)
    else:
        # if no ingredient is retrieved from db, return error
        return {'error': 'Ingredient not found'}, 404


@ingredients_bp.route('/<int:ingredient_id>', methods=['DELETE'])
@jwt_required()
def delete_ingredient(ingredient_id):
    # allows admin to delete an ingredient from database
    
    # admin access only
    admin_required()

    # build query: select ingredient with matching id
    stmt = db.select(Ingredient).filter_by(id=ingredient_id)
    # execute query and return a scalar result
    ingredient = db.session.scalar(stmt)

    if ingredient:
        # delete ingredient instance and commit changes to db
        db.session.delete(ingredient)
        db.session.commit()
        # return success message
        return {'message': f'Ingredient {ingredient_id} deleted'}, 200
    else:
        # if no ingredient is retrieved from db, return error
        return {'error': 'Ingredient not found'}, 404
