from flask import abort
from init import db, ma
from marshmallow import fields, validates_schema
from marshmallow.validate import Length, ValidationError

VALID_TYPES = ['Meat', 'Seafood', 'Derivatives', 'Grains', 'Vegetables', 'Other']


food_ingredient = db.Table('food_ingredient',
                           db.Column('food_id', db.Integer,
                                     db.ForeignKey('food.id', ondelete='CASCADE'), primary_key=True),
                           db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id', ondelete='CASCADE'), primary_key=True))


class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(30))

    food = db.relationship(
        'Food', secondary=food_ingredient, back_populates='ingredients')


class IngredientSchema(ma.Schema):

    name = fields.String(required=True,
                         validate=Length(min=2, max=100))

    category = fields.String()

    food = fields.List(fields.Nested(
        'FoodSchema', exclude=['notes', 'ingredients']))

    @validates_schema()
    def validate_food_type(self, data, **kwargs):
        # only validate when category is in the request body
        if data.get('category'):
            category = [x for x in VALID_TYPES if x.upper() ==
                        data['category'].upper()]
            if len(category) == 0:
                raise ValidationError(
                    f'Category must be one of: {VALID_TYPES}')
            data['category'] = category[0]

    class Meta:
        fields = ('id', 'name', 'category', 'food')
        ordered = True