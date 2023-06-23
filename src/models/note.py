from init import db, ma
from marshmallow import fields, validates_schema
from datetime import date
from marshmallow.validate import Length, OneOf, And, Regexp, ValidationError


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    date_created = db.Column(db.Date, default=date.today())
    is_negative = db.Column(db.Boolean, default=False)

    # create_by = db.Column(db.Integer, db.ForeignKey(
    #     'users.id', ondelete='CASCADE', nullable=False))

    cat_id = db.Column(db.Integer, db.ForeignKey(
        'cats.id', ondelete='CASCADE'), nullable=False)
    cat = db.relationship('Cat', back_populates='notes')

    food_id = db.Column(db.Integer, db.ForeignKey(
        'food.id', ondelete='CASCADE'), nullable=False)
    food = db.relationship('Food', back_populates='notes')


class NoteSchema(ma.Schema):
    cat = fields.Nested('CatSchema', exclude=[
        'year_born', 'year_adopted', 'notes'])

    food = fields.Nested('FoodSchema', exclude=['notes'])

    is_negative = fields.Boolean(load_default=False)

    cat_id = fields.Integer(required=True)

    food_id = fields.Integer(required=True)

    class Meta:
        fields = ('id', 'message', 'date_created',
                  'is_negative', 'cat_id', 'cat', 'food_id', 'food', 'created_by')
