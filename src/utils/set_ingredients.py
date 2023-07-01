from models.ingredient import Ingredient
from init import db
from flask import abort

def set_ingredients(food, ingredients_info):
    # check if input includes ingredients field
    
    if ingredients_info:
        # reset ingredients
        food.ingredients = []
        
        # go through input list and add each ingredient
        for ingredient in ingredients_info:
            # check if input includes id
            if ingredient.get('id'):
                # build query: select ingredient with matching id
                stmt = db.select(Ingredient).filter_by(
                    id=ingredient['id'])
                # execute query and return scalar result
                ingredient_from_id = db.session.scalar(stmt)
                
                # if no ingredient is retrieved, return error
                if not ingredient_from_id:
                    abort(400, description=f'ingredient_id {ingredient["id"]} not found')
                
                # if ingredient is not yet in field, add to the field
                elif ingredient_from_id not in food.ingredients:
                    food.ingredients.append(ingredient_from_id)
    return food.ingredients
