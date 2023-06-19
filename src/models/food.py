from init import db, ma
from marshmallow import fields


class Food(db.Model):
    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    name = db.Column(db.String, nullable=False, unique=True)
    brand = db.Column(db.String)

    notes = db.relationship(
        'Note', back_populates='food', cascade='all, delete')


class FoodSchema(ma.Schema):
    notes = fields.List(fields.Nested('NoteSchema', exclude=[
        'food']))

    class Meta:
        fields = ('id', 'type', 'name', 'brand', 'notes')
