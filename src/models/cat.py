from init import db, ma
from marshmallow import fields, validates_schema
from marshmallow.validate import Length, Range, ValidationError
from datetime import date


class Cat(db.Model):
    # use sqlalchemy's model to create a table structure with column names and data types

    # set the name of the table following naming convention
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year_born = db.Column(db.Integer)
    year_adopted = db.Column(db.Integer)
    breed = db.Column(db.String(100))

    owner_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    
    # establish one-to-many relationship: one user can have many cats
    owner = db.relationship('User', back_populates='cats')

    # establish one-to-many relationship: one cat can have many notes
    # notes will be deleted when cat is removed
    notes = db.relationship(
        'Note', back_populates='cat', cascade='all, delete')


class CatSchema(ma.Schema):
    # marshmallow schema is used for serializing and deserializing data, 
    # as well as validating and sanitizing user input
    name = fields.String(required=True,
                         validate=Length(max=100))

    # year_born must be between 1900 to current year
    year_born = fields.Integer(validate=Range(min=1900, max=date.today().year))

    # year_born must be between 1900 to current year
    year_adopted = fields.Integer(
        validate=Range(min=1900, max=date.today().year))

    # breed must be 5-100 characters
    breed = fields.String(validate=Length(min=5, max=100))

    # only show username of the owner and hide other information
    owner = fields.Nested('UserSchema', only=[
                          'username'])

    # exclude field to avoid unwanted recursion
    notes = fields.List(fields.Nested('NoteSchema', exclude=[
        'cat']))

    @validates_schema
    def validate_years(self, data, **kwargs):
        # only check when input includes both fields
        if data.get('year_born') and data.get('year_adopted'):
            # check that year_adopted must come after year_born
            if data["year_born"] > data["year_adopted"]:
                # if not, raise validation error
                raise ValidationError(
                    "year_adopted must be the same or later than year_born")

    class Meta:
        fields = ('id', 'name', 'breed', 'year_born',
                  'year_adopted', 'owner_id', 'owner', 'notes')
        # serialized result will follow the order in the fields 
        ordered = True
