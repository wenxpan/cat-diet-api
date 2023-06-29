from init import db, ma
from marshmallow import fields, validates_schema
from marshmallow.validate import Length, ValidationError
from models.ingredient import food_ingredient

# set up a constant outlining all the valid categories of foods
VALID_TYPES = ['Wet', 'Dry', 'Freeze-dried',
               'Raw', 'Cooked', 'Treats']


class Food(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    brand = db.Column(db.String(100))
    category = db.Column(db.String(30))
    notes = db.relationship(
        'Note', back_populates='food', cascade='all, delete')
    ingredients = db.relationship('Ingredient', secondary=food_ingredient, back_populates='foods')

class FoodSchema(ma.Schema):
    # marshmallow schema is used for serializing and deserializing data, 
    # as well as validating and sanitizing user input
    notes = fields.List(fields.Nested('NoteSchema', exclude=[
        'food_id', 'food', 'cat_id']))

    name = fields.String(required=True,
                         validate=Length(min=2, max=200))

    brand = fields.String(validate=Length(min=2, max=100))

    category = fields.String()

    ingredients = fields.List(fields.Nested(
        'IngredientSchema', exclude=['foods']))

    @validates_schema()
    def validate_category(self, data, **kwargs):
        # only validate when category is in the request body
        if data.get('category'):
            category = [x for x in VALID_TYPES if x.upper() ==
                        data['category'].upper()]
            if len(category) == 0:
                raise ValidationError(
                    f'Food_type must be one of: {VALID_TYPES}')
            data['category'] = category[0]

    class Meta:
        fields = ('id', 'name', 'brand', 'category', 'ingredients', 'notes')
        ordered = True