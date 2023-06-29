from init import db, ma
from marshmallow import fields, validates_schema
from marshmallow.validate import Length
from models.ingredient import food_ingredient
from utils.check_input import check_input_category

# set up a constant outlining all the valid categories of foods
VALID_CATEGORIES = ['Wet', 'Dry', 'Freeze-dried',
               'Raw', 'Cooked', 'Treats']


class Food(db.Model):
    # use sqlalchemy's model to create a table structure with column names and data types

    # set the name of the table following naming convention
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    brand = db.Column(db.String(100))
    category = db.Column(db.String(30))
    
    # establish many-to-many relationship using join table
    # one food can have many ingredients, one ingredient can make many foods
    ingredients = db.relationship(
        'Ingredient', secondary=food_ingredient, back_populates='foods')

    # establish one-to-many relationship: one food can have many notes
    # notes will be removed when the food is deleted
    notes = db.relationship(
        'Note', back_populates='food', cascade='all, delete')

class FoodSchema(ma.Schema):
    # marshmallow schema is used for serializing and deserializing data, 
    # as well as validating and sanitizing user input

    # set length limit for name
    name = fields.String(required=True,
                         validate=Length(min=2, max=200))

    # set length limit for brand
    brand = fields.String(validate=Length(min=2, max=100))

    # check category is a string before making it uppercase in the validate function below
    category = fields.String()

    # exclude foods fields in ingredients to avoid recursion
    ingredients = fields.List(fields.Nested(
        'IngredientSchema', exclude=['foods']))

    notes = fields.List(fields.Nested('NoteSchema', exclude=[
        'food_id', 'food', 'cat_id']))
    
    @validates_schema()
    def validate_category(self, data, **kwargs):
        # check that input category belongs to one of the set types
        check_input_category(data, VALID_CATEGORIES)

    class Meta:
        fields = ('id', 'name', 'brand', 'category', 'ingredients', 'notes')
        # serialized result will follow the order in the fields 
        ordered = True