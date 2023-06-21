from init import db, ma
from marshmallow import fields


class Cat(db.Model):
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    year_born = db.Column(db.String)
    year_adopted = db.Column(db.String)
    breed = db.Column(db.String)

    # one user can have many cats; cascade delete
    owner_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    owner = db.relationship('User', back_populates='cats')

    notes = db.relationship(
        'Note', back_populates='cat', cascade='all, delete')


class CatSchema(ma.Schema):
    owner = fields.Nested('UserSchema', exclude=[
                          'password', 'email', 'is_admin', 'cats'])

    notes = fields.List(fields.Nested('NoteSchema', exclude=[
        'cat']))

    class Meta:
        fields = ('id', 'name', 'breed', 'year_born',
                  'year_adopted', 'owner_id', 'owner', 'notes')
