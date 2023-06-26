from flask import Blueprint
from init import db
from models.food import Food, FoodSchema
from models.ingredient import Ingredient, IngredientSchema
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required
from flask import request
from sqlalchemy.exc import IntegrityError

food_bp = Blueprint('food', __name__, url_prefix='/food')


@food_bp.route('/')
def all_food():
    stmt = db.select(Food)
    food = db.session.scalars(stmt)
    return FoodSchema(many=True).dump(food)


@food_bp.route('/', methods=['POST'])
@jwt_required()
def create_food():
    try:
        print('processed1')
        food_info = FoodSchema().load(request.json, partial=True)
        print('processed2')
        food = Food(
            name=food_info['name'],
            food_type=food_info.get('food_type'),
            brand=food_info.get('brand'),
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
        return FoodSchema(exclude=['notes']).dump(food), 201
    except IntegrityError:
        # maybe add a function to return the food id
        return {'error': 'Food name already exists'}


@food_bp.route('/<int:food_id>')
def get_one_food(food_id):
    stmt = db.select(Food).filter_by(id=food_id)
    food = db.session.scalar(stmt)
    if food:
        return FoodSchema().dump(food)
    else:
        return {'error': 'Food not found'}, 404


@food_bp.route('/<int:food_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(food_id):
    admin_required()
    stmt = db.select(Food).filter_by(id=food_id)
    food = db.session.scalar(stmt)
    food_info = FoodSchema().load(request.json, partial=True)
    if food:
        food.name = food_info.get('name', food.name)
        food.food_type = food_info.get('food_type', food.food_type)
        food.brand = food_info.get('brand', food.brand)
        db.session.commit()
        return FoodSchema(exclude=['notes']).dump(food)
    else:
        return {'error': 'Food not found'}, 404


@food_bp.route('/<int:food_id>', methods=['DELETE'])
@jwt_required()
def delete_user(food_id):
    admin_required()
    stmt = db.select(Food).filter_by(id=food_id)
    food = db.session.scalar(stmt)
    if food:
        db.session.delete(food)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Food not found'}, 404
