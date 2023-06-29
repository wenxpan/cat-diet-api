from init import db
from models.cat import Cat
from models.food import Food
from models.note import Note

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
