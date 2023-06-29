from init import db, ma
from marshmallow import fields
from datetime import date
from marshmallow.validate import Range


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
        'foods.id', ondelete='CASCADE'), nullable=False)
    food = db.relationship('Food', back_populates='notes')


class NoteSchema(ma.Schema):
    # marshmallow schema is used for serializing and deserializing data, 
    # as well as validating and sanitizing user input
    
    cat = fields.Nested('CatSchema', exclude=[
        'year_born', 'year_adopted', 'notes', 'owner_id'])

    food = fields.Nested('FoodSchema', exclude=['notes'])

    rating = fields.Integer(
        load_default=0, validate=Range(min=-1, max=1))

    cat_id = fields.Integer(required=True)

    food_id = fields.Integer(required=True)

    date_recorded = fields.Date(load_default=date.today())

    class Meta:
        fields = ('id', 'cat_id', 'cat', 'food_id', 'food', 'rating', 'message', 'date_recorded')
        ordered = True
