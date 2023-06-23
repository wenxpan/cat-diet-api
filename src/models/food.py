from init import db, ma
from marshmallow import fields, validates_schema
from marshmallow.validate import Length, OneOf, And, Regexp, ValidationError

VALID_TYPES = ['Wet', 'Dry', 'Freeze-dried', 'Raw', 'Home cooked']


class Food(db.Model):
    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30))
    name = db.Column(db.String(200), nullable=False, unique=True)
    brand = db.Column(db.String(100), default='Unbranded')
    notes = db.relationship(
        'Note', back_populates='food', cascade='all, delete')


class FoodSchema(ma.Schema):
    notes = fields.List(fields.Nested('NoteSchema', exclude=[
        'food']))

    name = fields.String(required=True,
                         validate=Length(min=2, max=200, error='name must be 2-200 characters long'))

    brand = fields.String(load_default='Unbranded',
                          validate=Length(min=2, max=100, error='brand must be 2-100 characters long'))

    @validates_schema()
    def validate_type(self, data, **kwargs):
        type = [x for x in VALID_TYPES if x.upper() == data['type'].upper()]
        if len(type) == 0:
            raise ValidationError(
                f'Status must be one of: {VALID_TYPES}')
        data['type'] = type[0]

    class Meta:
        fields = ('id', 'type', 'name', 'brand', 'notes')
