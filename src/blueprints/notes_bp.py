from flask import Blueprint, request
from init import db
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
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

    # build query: select note with matching id
    stmt = db.select(Note).filter_by(id=note_id)
    # execute query and return a scalar result
    note = db.session.scalar(stmt)
    if note:
        # return seraialized result
        return NoteSchema().dump(note)
    else:
        # if no note is retrieved from db, return error
        return {'error': 'Note not found'}, 404


@notes_bp.route('/<int:note_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_note(note_id):
    # update note information of the selected id

    # build query: select note with matching id
    stmt = db.select(Note).filter_by(id=note_id)
    # execute query and return a scalar result
    note = db.session.scalar(stmt)

    if note:
        # check if the token user is admin or cat owner (i.e. the one who created note)
        admin_or_owner_required(note.cat.owner_id)

        # load data using schema to sanitize and validate input
        note_info = NoteSchema().load(request.json, partial=True)

        # if cat id is to be updated, check the cat owner stays the same
        if note_info.get('cat_id'):

            # build query: select owner_id column from table cats
            # with cat's id matching updated cat_id in the request body
            new_stmt = db.select(Cat.owner_id).filter_by(id=note_info.get('cat_id'))
            # execute query and return a scalar result (integer)
            new_cat_owner = db.session.scalar(new_stmt)

            # if cat owner not found (i.e. cat does not exist), return error
            if not new_cat_owner:
                return {'error': 'Invalid cat_id: Cat not found'}, 400
            else:
                # build query: select owner_id column from table cats 
                # with cat's id matching the cat_id in the original note
                org_stmt = db.select(Cat.owner_id).filter_by(id=note.cat.id)
                # execute query and return a scalar result (integer)
                original_cat_owner = db.session.scalar(org_stmt)

                # check if the cat owner is the same, return error if not
                if original_cat_owner != new_cat_owner:
                    return {'error': 'The user is not the owner of the cat'}, 400

        # update note
        try:
            note.message = note_info.get('message', note.message)
            note.rating = note_info.get('rating', note.rating)
            note.cat_id = note_info.get('cat_id', note.cat_id)
            note.food_id = note_info.get('food_id', note.food_id)
            note.date_recorded = note_info.get('date_recorded', note.date_recorded)
            
            # commit changes to db
            db.session.commit()
        except IntegrityError:
            # return error if food_id not found in db
            return {'error': 'Invalid food_id: Food not found'}, 400
        
        # return updated food
        return NoteSchema(exclude=['cat_id', 'food_id']).dump(note)
    else:
        # if no note is retrieved from db, return error
        return {'error': 'Note not found'}, 404


@notes_bp.route('/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note(note_id):
    # allows admin or owner to delete a note from database
    
    # build query: select note with matching id
    stmt = db.select(Note).filter_by(id=note_id)
    # execute query and return a scalar result
    note = db.session.scalar(stmt)

    if note:
        # check if the token user is admin or cat owner
        admin_or_owner_required(note.cat.owner.id)

        # delete note instance and commit changes to db
        db.session.delete(note)
        db.session.commit()

        # return success message
        return {'message': f'Note {note_id} deleted'}, 200
    else:
        # if no note is retrieved from db, return error
        return {'error': 'Note not found'}, 404
