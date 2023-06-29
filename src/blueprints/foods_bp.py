from flask import Blueprint
from init import db
from models.food import Food, FoodSchema
from models.ingredient import Ingredient, IngredientSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_required
from flask import request
from sqlalchemy.exc import IntegrityError

foods_bp = Blueprint('food', __name__, url_prefix='/foods')


@foods_bp.route('/')
def all_foods():
    # returns a list of foods with their ingredients and related notes

    stmt = db.select(Food)
    foods = db.session.scalars(stmt)
    return FoodSchema(many=True).dump(foods)


@foods_bp.route('/', methods=['POST'])
@jwt_required()
def create_food():
    # creates a new food in the database

    try:
        print('processed1')
        food_info = FoodSchema().load(request.json, partial=True)
        print('processed2')
        food = Food(
            name=food_info['name'],
            category=food_info.get('category'),
            brand=food_info.get('brand'),
            created_by=get_jwt_identity(),
            last_modified_by=get_jwt_identity()
        )
        ingredients_info = food_info.get('ingredients')
        if ingredients_info:
            for ingredient in ingredients_info:
                if ingredient.get('id'):
                    stmt = db.select(Ingredient).filter_by(
                        id=ingredient['id'])
                    ingredient_from_id = db.session.scalar(stmt)
                    if not ingredient_from_id:
                        return {'error': 'ingredient id not found'}, 400
                    elif ingredient_from_id in food.ingredients:
                        pass
                    else:
                        food.ingredients.append(ingredient_from_id)
        db.session.add(food)
        db.session.commit()
        return FoodSchema().dump(food), 201
    except IntegrityError:
        return {'error': 'Food name already exists'}


@foods_bp.route('/<int:food_id>')
def get_one_food(food_id):
    # returns food of the selected id


    stmt = db.select(Food).filter_by(id=food_id)
    food = db.session.scalar(stmt)
    if food:
        return FoodSchema().dump(food)
    else:
        return {'error': 'Food not found'}, 404


@foods_bp.route('/<int:food_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_food(food_id):
    # updates food information of the selected id

    admin_required()
    stmt = db.select(Food).filter_by(id=food_id)
    food = db.session.scalar(stmt)
    food_info = FoodSchema().load(request.json, partial=True)
    if food:
        food.name = food_info.get('name', food.name)
        food.category = food_info.get('category', food.category)
        food.brand = food_info.get('brand', food.brand)
        food.last_modified_by = get_jwt_identity()

        # make it dry
        ingredients_info = food_info.get('ingredients')
        if ingredients_info:
            food.ingredients = []
            for ingredient in ingredients_info:
                if ingredient.get('id'):
                    stmt = db.select(Ingredient).filter_by(
                        id=ingredient['id'])
                    ingredient_from_id = db.session.scalar(stmt)
                    if not ingredient_from_id:
                        return {'error': f"ingredient id {ingredient['id']} not found"}, 400
                    elif ingredient_from_id in food.ingredients:
                        pass
                    else:
                        food.ingredients.append(ingredient_from_id)
        db.session.commit()
        return FoodSchema(exclude=['notes']).dump(food)
    else:
        return {'error': 'Food not found'}, 404


@foods_bp.route('/<int:food_id>', methods=['DELETE'])
@jwt_required()
def delete_food(food_id):
    # allows admin to delete a food from database
    
    admin_required()
    stmt = db.select(Food).filter_by(id=food_id)
    food = db.session.scalar(stmt)
    if food:
        db.session.delete(food)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Food not found'}, 404
