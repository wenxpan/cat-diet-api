from flask import Blueprint
from init import db
from models.food import Food, FoodSchema
from models.ingredient import Ingredient, IngredientSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.authorise import admin_required
from utils.set_ingredient import set_ingredient
from flask import request
from sqlalchemy.exc import IntegrityError

# create blueprint for the /foods endpoint
foods_bp = Blueprint('food', __name__, url_prefix='/foods')


@foods_bp.route('/')
def all_foods():
    # returns a list of foods with their ingredients and related notes

    # build query: select all foods from foods table
    stmt = db.select(Food)
    # execute query and return scalars result
    foods = db.session.scalars(stmt)

    # return serialized result
    return FoodSchema(many=True).dump(foods)


@foods_bp.route('/', methods=['POST'])
@jwt_required()
def create_food():
    # creates a new food in the database

    try:
        # load data using schema to sanitize and validate input
        food_info = FoodSchema().load(request.json, partial=True)

        # create a new Food model instance
        food = Food(
            name=food_info['name'],
            brand=food_info.get('brand'), # optional
            category=food_info.get('category'), # optional
        )

        food.ingredients = set_ingredient(food, food_info.get('ingredients'))

        # add and commit food to db
        db.session.add(food)
        db.session.commit()

        # return serialized result
        return FoodSchema().dump(food), 201
    except IntegrityError:
        # if food name is not unique, return error
        return {'error': 'Food name already exists'}, 409


@foods_bp.route('/<int:food_id>')
def get_one_food(food_id):
    # returns food of the selected id

    # build query: select food with matching id
    stmt = db.select(Food).filter_by(id=food_id)
    # execute query and return a scalar result
    food = db.session.scalar(stmt)
    if food:
        # return seraialized result
        return FoodSchema().dump(food)
    else:
        # if no food is retrieved from db, return error
        return {'error': 'Food not found'}, 404


@foods_bp.route('/<int:food_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_food(food_id):
    # updates food information of the selected id

    # admin access only
    admin_required()

    # build query: select food with matching id
    stmt = db.select(Food).filter_by(id=food_id)
    # execute query and return a scalar result
    food = db.session.scalar(stmt)

    if food:
        # load data using schema to sanitize and validate input
        food_info = FoodSchema().load(request.json, partial=True)

        # all fields can be optional, so get methods are used
        food.name = food_info.get('name', food.name)
        food.category = food_info.get('category', food.category)
        food.brand = food_info.get('brand', food.brand)

        food.ingredients = set_ingredient(food, food_info.get('ingredients'))

        # commit changes to db
        db.session.commit()

        # return update food
        return FoodSchema(exclude=['notes']).dump(food)
    else:
        # if no food is retrieved from db, return error
        return {'error': 'Food not found'}, 404


@foods_bp.route('/<int:food_id>', methods=['DELETE'])
@jwt_required()
def delete_food(food_id):
    # allows admin to delete a food from database

    # admin access only
    admin_required()

    # build query: select food with matching id
    stmt = db.select(Food).filter_by(id=food_id)
    # execute query and return a scalar result
    food = db.session.scalar(stmt)

    if food:
        # delete food instance and commit changes to db
        db.session.delete(food)
        db.session.commit()

        # return success message
        return {'message': f'Food {food_id} and related notes deleted'}, 200
    else:
        # if no food is retrieved from db, return error
        return {'error': 'Food not found'}, 404
