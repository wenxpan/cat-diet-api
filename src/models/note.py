from init import db, ma
from marshmallow import fields
from marshmallow.validate import Range
from datetime import date


class Note(db.Model):
    # use sqlalchemy's model to create a table structure with column names and data types

    # set the name of the table following naming convention
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    rating = db.Column(db.Integer, default=0)
    date_recorded = db.Column(db.Date, default=date.today())

    # one note can only talk about one cat
    # note will be deleted when cat is removed
    cat_id = db.Column(db.Integer, db.ForeignKey(
        'cats.id', ondelete='CASCADE'), nullable=False)    
    cat = db.relationship('Cat', back_populates='notes')

    # one note can only talk about one food 
    # note will be deleted when food is removed
    food_id = db.Column(db.Integer, db.ForeignKey(
        'foods.id', ondelete='CASCADE'), nullable=False)
    food = db.relationship('Food', back_populates='notes')


class NoteSchema(ma.Schema):
    # marshmallow schema is used for serializing and deserializing data, 
    # as well as validating and sanitizing user input

    # rating must be -1, 0, or 1, and default is 0 (neutral)
    rating = fields.Integer(
        load_default=0, validate=Range(min=-1, max=1))

    # date must be no later than today, and default is today
    date_recorded = fields.Date(load_default=date.today(), 
                                validate=Range(max=date.today()))
    
    cat_id = fields.Integer(required=True)
    cat = fields.Nested('CatSchema', only=['id', 'name', 'breed', 'owner'])

    food_id = fields.Integer(required=True)
    food = fields.Nested('FoodSchema', exclude=['notes'])

    class Meta:
        fields = ('id', 'message', 'rating', 'date_recorded', 
                  'cat_id', 'cat', 'food_id', 'food')
        # serialized result will follow the order in the fields 
        ordered = True
