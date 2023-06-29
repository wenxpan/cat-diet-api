from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp
from datetime import date
from models.cat import Cat
from models.food import Food
from models.note import Note


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    joined_since = db.Column(db.Date, default=date.today())

    cats = db.relationship('Cat', back_populates='owner',
                           cascade='all, delete')


class UserSchema(ma.Schema):

    username = fields.String(
        required=True, validate=Regexp(
            '^[a-zA-Z0-9_-]{3,15}$',
            error='Username must be 3-15 characters long and contain letters, numbers, underscores and dashes only'))
    
    email = fields.Email(required=True)

    password = fields.String(required=True, validate=Regexp(
        '^(?=.*?[a-zA-Z])(?=.*?[0-9]).{8,32}$',
        error='Password must be 8-32 characters long and must contain at least one English letter and one number.'))

    is_admin = fields.Boolean(load_default=False)

    cats = fields.List(fields.Nested('CatSchema', exclude=['owner_id', 'owner', 'notes']))

    class Meta:
        fields = ('id', 'username', 'email', 'password',
                  'is_admin', 'joined_since', 'cats')
        ordered = True


def get_user_statistics(user_id):
    cats_stmt = db.select(db.func.count()).select_from(
        Cat).filter(Cat.owner_id == user_id)
    total_cats = db.session.scalar(cats_stmt)

    notes_stmt = db.select(db.func.count()).select_from(Cat).join(
        Cat.notes).filter(Cat.owner_id == user_id)
    total_notes = db.session.scalar(notes_stmt)

    food_stmt = db.select(db.func.count(db.distinct(Food.id))).select_from(Cat).join(Cat.notes).join(Note.food).where(Cat.owner_id == user_id)
    total_foods = db.session.scalar(food_stmt)

    return {
        'total_cats': total_cats,
        'total_notes': total_notes,
        'total_foods_reviewed': total_foods
    }
