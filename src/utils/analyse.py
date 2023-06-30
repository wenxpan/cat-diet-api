from init import db
from models.cat import Cat
from models.food import Food
from models.note import Note


def get_user_statistics(user_id):
    # used in /users routes to show user statistics based on data from db

    # build query: select total count of cats from cats table,
    # filtered by cat's owner_id matching the queried user_id
    cats_stmt = db.select(db.func.count()).select_from(
        Cat).filter(Cat.owner_id == user_id)
    # execute query and return a scalar result (integer, total cats owned by the user)
    total_cats = db.session.scalar(cats_stmt)

    # build query: select total count of notes from cats JOIN notes,
    # filtered by cat's owner_id matching the queried user_id
    notes_stmt = db.select(db.func.count()).select_from(Cat).join(
        Cat.notes).filter(Cat.owner_id == user_id)
    # execute query and return a scalar result (integer, total notes created by the user)
    total_notes = db.session.scalar(notes_stmt)

    # build query: select count of distinct food from cats JOIN notes JOIN 
    # food table, filtered by cat's owner_id matching the queried user_id
    food_stmt = db.select(db.func.count(
        db.distinct(Food.id))).select_from(
        Cat).join(Cat.notes).join(
        Note.food).where(Cat.owner_id == user_id)
    # execute query and return a scalar result (integer, total food reviewed by the user)
    total_foods = db.session.scalar(food_stmt)

    return {
        'total_cats': total_cats,
        'total_notes': total_notes,
        'total_foods_reviewed': total_foods
    }


