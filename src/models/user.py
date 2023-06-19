from init import db, ma
from marshmallow import fields


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    cats = db.relationship('Cat', back_populates='owner',
                           cascade='all, delete')


class UserSchema(ma.Schema):
    cats = fields.List(fields.Nested('CatSchema', exclude=['id', 'owner']))

    class Meta:
        fields = ('id', 'username', 'email', 'password', 'is_admin', 'cats')
        ordered = True
