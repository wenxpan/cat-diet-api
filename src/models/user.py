from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, OneOf, And, Regexp
from datetime import date


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    joined_since = db.Column(db.Date, default=date.today())

    cats = db.relationship('Cat', back_populates='owner',
                           cascade='all, delete')


class UserSchema(ma.Schema):
    cats = fields.List(fields.Nested('CatSchema', exclude=['owner']))

    email = fields.String(required=True, validate=Regexp(
        '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+', error='Please provide a valid email address'))

    password = fields.String(required=True, validate=Regexp(
        '^(?=.*?[a-zA-Z])(?=.*?[0-9]).{8,32}$',
        error='Password must be 8-32 characters long and must contain at least one English letter and one number.'))

    username = fields.String(
        required=True, validate=Regexp(
            '^[a-zA-Z0-9_-]{3,15}$',
            error='Username must be 3-15 characters long and contain letters, numbers, underscores and dashes only'))

    is_admin = fields.Boolean(load_default=False)

    class Meta:
        fields = ('id', 'username', 'email', 'password',
                  'is_admin', 'cats', 'joined_since')
        ordered = True


def get_user_statistics():
    return {
        'total_cats': 2,
        'total_notes': 3,
        'total_food_reviewed': 4,
        'most_positive_food': 'xx',
        'most_negative_food': 'xx'
    }
