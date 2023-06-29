from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp
from datetime import date



class User(db.Model):
    # use sqlalchemy's model to create a table structure with column names and data types

    # set the name of the table following naming convention
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    joined_since = db.Column(db.Date, default=date.today())

    # establish one-to-many relationship: one user can have many cats
    # cats will be removed when their owner is deleted
    cats = db.relationship('Cat', back_populates='owner',
                           cascade='all, delete')


class UserSchema(ma.Schema):
    # marshmallow schema is used for serializing and deserializing data, 
    # as well as validating and sanitizing user input

    # use regular expression to validate username
    username = fields.String(
        required=True, validate=Regexp(
            '^[a-zA-Z0-9_-]{3,15}$',
            error='Username must be 3-15 characters long and contain letters, numbers, underscores and dashes only'))
    
    # use marshmallow's built in email field to validate email address
    email = fields.Email(required=True)

    # use regular expression to validate password
    password = fields.String(required=True, validate=Regexp(
        '^(?=.*?[a-zA-Z])(?=.*?[0-9]).{8,32}$',
        error='Password must be 8-32 characters long and must contain at least one English letter and one number.'))

    # load default will set is_admin to False if the field is empty
    is_admin = fields.Boolean(load_default=False)

    cats = fields.List(fields.Nested('CatSchema', exclude=['owner_id', 'owner', 'notes']))

    class Meta:
        fields = ('id', 'username', 'email', 'password',
                  'is_admin', 'joined_since', 'cats')
        # serialized result will follow the order in the fields 
        ordered = True