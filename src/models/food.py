from init import db, ma
from marshmallow import fields, validates_schema
from marshmallow.validate import Length, OneOf, And, Regexp, ValidationError
from models.ingredient import Ingredient, food_ingredient


VALID_TYPES = ['Wet', 'Dry', 'Freeze-dried', 'Raw', 'Home cooked']


class Food(db.Model):
    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    food_type = db.Column(db.String(30))
    name = db.Column(db.String(200), nullable=False, unique=True)
    brand = db.Column(db.String(100), default='Unbranded')
    notes = db.relationship(
        'Note', back_populates='food', cascade='all, delete')


class FoodSchema(ma.Schema):
    notes = fields.List(fields.Nested('NoteSchema', exclude=[
        'food']))

    name = fields.String(required=True,
                         validate=Length(min=2, max=200))

    brand = fields.String(load_default='Unbranded',
                          validate=Length(min=2, max=100))

    food_type = fields.String(required=True)

    ingredients = db.relationship(
        'Ingredient', secondary=food_ingredient, backref='food')

    @validates_schema()
    def validate_food_type(self, data, **kwargs):
        # only validate when food_type is in the request body
        if data.get('food_type'):
            food_type = [x for x in VALID_TYPES if x.upper() ==
                         data['food_type'].upper()]
            if len(food_type) == 0:
                raise ValidationError(
                    f'Food_type must be one of: {VALID_TYPES}')
            data['food_type'] = food_type[0]

    class Meta:
        fields = ('id', 'food_type', 'name', 'brand', 'notes')
