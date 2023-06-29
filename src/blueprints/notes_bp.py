from flask import Blueprint, request
from init import db
from flask_jwt_extended import jwt_required
from datetime import date
from models.note import Note, NoteSchema
from models.cat import Cat
from models.food import Food
from utils.authorise import admin_or_owner_required

# create blueprint for the /notes endpoint
notes_bp = Blueprint('notes', __name__, url_prefix='/notes')


@notes_bp.route('/')
def all_notes():
    # returns a list of notes, each with its related cat and food information
    
    # build query: select all notes from notes table
    stmt = db.select(Note)
    # execute query and return scalars result
    notes = db.session.scalars(stmt)

    # return serialized result
    return NoteSchema(many=True, exclude=['cat_id', 'food_id']).dump(notes)


@notes_bp.route('/', methods=['POST'])
@jwt_required()
def create_note():
    # create a new note in the database

    # load data using schema to sanitize and validate input
    note_info = NoteSchema().load(request.json)

    # select cat and food with matching id
    cat = db.session.scalar(db.select(Cat).filter_by(
        id=note_info.get('cat_id')))
    food = db.session.scalar(
        db.select(Food).filter_by(id=note_info.get('food_id')))
    # if cat or food or both do not exist, return erro
    if not cat or not food:
        return {'error': 'Cat or food not found'}, 400
    else:
        # check if the token identity is the cat owner
        admin_or_owner_required(cat.owner_id)

        # create a new Note model instance
        note = Note(
            rating=note_info.get('rating'), # optional
            message=note_info.get('message'), # optional
            cat_id=note_info['cat_id'],
            food_id=note_info['food_id'],
            # if date_recorded is empty, set the default to today
            date_recorded=note_info.get('date_recorded', date.today())
        )

        # add and commit note to db
        db.session.add(note)
        db.session.commit()

        # return serialized result
        return NoteSchema(exclude=['cat_id', 'food_id']).dump(note), 201


@notes_bp.route('/<int:note_id>')
def get_one_note(note_id):
    # returns note of the selected id and the related cat and food information

    stmt = db.select(Note).filter_by(id=note_id)
    note = db.session.scalar(stmt)
    if note:
        return NoteSchema().dump(note)
    else:
        return {'error': 'Note not found'}, 404


@notes_bp.route('/<int:note_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_note(note_id):
    # update note information of the selected id

    note_info = NoteSchema().load(request.json, partial=True)

    stmt = db.select(Note).filter_by(id=note_id)
    note = db.session.scalar(stmt)

    if note:
        admin_or_owner_required(note.cat.owner_id)
        # make this part dry
        if note_info.get('cat_id'):
            stmt = db.select(Cat).filter_by(
                id=note_info.get('cat_id'))
            updated_cat = db.session.scalar(stmt)
            if updated_cat:
                admin_or_owner_required(updated_cat.owner_id)
            else:
                return {'error': 'Cat not found'}, 404

        elif note_info.get('food_id'):
            stmt = db.select(Food).filter_by(id=note_info.get('food_id'))
            updated_food = db.session.scalar(stmt)
            if not updated_food:
                return {'error': 'Food not found'}, 404

        else:
            note.message = note_info.get('message', note.message)
            note.rating = note_info.get('rating', note.rating)
            note.cat_id = note_info.get('cat_id', note.cat_id)
            note.food_id = note_info.get('food_id', note.food_id)
            note.date_recorded = note_info.get('date_recorded', note.date_recorded)
            db.session.commit()
            return NoteSchema(exclude=['cat_id', 'food_id']).dump(note)
    else:
        return {'error': 'Note not found'}, 404


@notes_bp.route('/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note(note_id):
    # allows admin or owner to delete a note from database
    
    stmt = db.select(Note).filter_by(id=note_id)
    note = db.session.scalar(stmt)
    if note:
        owner_id = note.cat.owner.id
        admin_or_owner_required(owner_id)
        db.session.delete(note)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Note not found'}, 404
