from init import db, ma
from marshmallow import fields, validates_schema
from datetime import date
from marshmallow.validate import Length, OneOf, And, Range, Regexp, ValidationError


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    rating = db.Column(db.Integer, default=0)

    date_recorded = db.Column(db.Date, default=date.today())

    cat_id = db.Column(db.Integer, db.ForeignKey(
        'cats.id', ondelete='CASCADE'), nullable=False)
    cat = db.relationship('Cat', back_populates='notes')

    food_id = db.Column(db.Integer, db.ForeignKey(
        'food.id', ondelete='CASCADE'), nullable=False)
    food = db.relationship('Food', back_populates='notes')


class NoteSchema(ma.Schema):
    cat = fields.Nested('CatSchema', exclude=[
        'year_born', 'year_adopted', 'notes', 'owner_id'])

    food = fields.Nested('FoodSchema', exclude=['notes'])

    rating = fields.Integer(
        load_default=0, validate=Range(min=-1, max=1))

    cat_id = fields.Integer(required=True)

    food_id = fields.Integer(required=True)

    date_recorded = fields.Date(load_default=date.today())

    class Meta:
        fields = ('id', 'message', 'rating', 'date_recorded',
                  'cat_id', 'cat', 'food_id', 'food')
