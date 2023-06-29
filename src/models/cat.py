from init import db, ma
from marshmallow import fields, validates_schema
from marshmallow.validate import Length, Range, OneOf, And, Regexp, ValidationError
from datetime import date


class Cat(db.Model):
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year_born = db.Column(db.Integer)
    year_adopted = db.Column(db.Integer)
    breed = db.Column(db.String(100))

    # one user can have many cats; cascade delete
    owner_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    owner = db.relationship('User', back_populates='cats')

    notes = db.relationship(
        'Note', back_populates='cat', cascade='all, delete')


class CatSchema(ma.Schema):
    # marshmallow schema is used for serializing and deserializing data, 
    # as well as validating and sanitizing user input
    owner = fields.Nested('UserSchema', only=[
                          'username'])

    notes = fields.List(fields.Nested('NoteSchema', exclude=[
        'cat']))

    name = fields.String(required=True,
                         validate=Length(max=100))

    year_born = fields.Integer(validate=Range(min=1900, max=date.today().year))

    year_adopted = fields.Integer(
        validate=Range(min=1900, max=date.today().year))

    breed = fields.String(validate=Length(min=5, max=100))

    @validates_schema
    def validate_numbers(self, data, **kwargs):
        if data["year_born"] >= data["year_adopted"]:
            raise ValidationError(
                "year_adopted must be greater than year_born")

    class Meta:
        fields = ('id', 'name', 'breed', 'year_born',
                  'year_adopted', 'owner_id', 'owner', 'notes')
        ordered = True
