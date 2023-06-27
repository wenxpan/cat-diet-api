from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, OneOf, And, Regexp
from datetime import date
from models.cat import Cat, CatSchema
from models.note import Note


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

    email = fields.Email(required=True)

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


def get_user_statistics(user_id):
    cats_stmt = db.select(db.func.count()).select_from(
        Cat).filter(Cat.owner_id == user_id)
    total_cats = db.session.scalar(cats_stmt)

    notes_stmt = db.select(db.func.count()).select_from(Cat).join(
        Cat.notes).filter(Cat.owner_id == user_id)
    total_notes = db.session.scalar(notes_stmt)

    food_stmt = db.select(db.func.count()).select_from(Cat).join(
        Cat.notes).join(Note.food).filter(
        Cat.owner_id == user_id).group_by(Note.food_id)
    total_food = db.session.scalar(food_stmt)

    return {
        'total_cats': total_cats,
        'total_notes': total_notes,
        'total_food_reviewed': total_food
    }
