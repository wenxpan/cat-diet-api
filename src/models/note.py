from init import db, ma
from marshmallow import fields


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    date_created = db.Column(db.Date)
    is_negative = db.Column(db.Boolean, default=False)

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

    class Meta:
        fields = ('id', 'message', 'date_created',
                  'is_negative', 'cat', 'food')
