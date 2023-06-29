from init import db, ma
from marshmallow import fields, validates_schema
from marshmallow.validate import Length
from utils.check_input import check_input_category


# set up a constant outlining all the valid categories of ingredients
VALID_CATEGORIES = ['Meat', 'Seafood', 'Derivatives', 'Grains', 'Vegetables', 'Other']


# create join table for many-to-many relationship between foods and ingredients
# food_id and ingredient_id will be primary keys with no additional attributes
food_ingredient = db.Table('food_ingredient',
                           db.Column('food_id', db.Integer,
                                     db.ForeignKey('foods.id', ondelete='CASCADE'), primary_key=True),
                           db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id', ondelete='CASCADE'), primary_key=True))


class Ingredient(db.Model):
    # use sqlalchemy's model to create a table structure with column names and data types

    # set the name of the table following naming convention
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(30))
    
    # establish many-to-many relationship using join table
    # one ingredient can make many foods, one food can have many ingredients
    foods = db.relationship(
        'Food', secondary=food_ingredient, back_populates='ingredients')


class IngredientSchema(ma.Schema):
    # marshmallow schema is used for serializing and deserializing data, 
    # as well as validating and sanitizing user input

    # set length limit for name
    name = fields.String(required=True,
                         validate=Length(min=2, max=100))

    # check category is a string before making it uppercase in the validate function below
    category = fields.String()

    # exclude less relevant fields and avoid unwanted recursion
    foods = fields.List(fields.Nested(
        'FoodSchema', exclude=['notes', 'ingredients']))

    @validates_schema()
    def validate_category(self, data, **kwargs):
        # check that input category belongs to one of the set types
        check_input_category(data, VALID_CATEGORIES)

    class Meta:
        fields = ('id', 'name', 'category', 'foods')
        # serialized result will follow the order in the fields
        ordered = True