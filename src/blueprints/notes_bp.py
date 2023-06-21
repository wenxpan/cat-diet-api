from flask import Blueprint
from init import db
from models.note import Note, NoteSchema
from models.cat import Cat, CatSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_required, admin_or_owner_required
from flask import request
from datetime import date


notes_bp = Blueprint('notes', __name__, url_prefix='/notes')


@notes_bp.route('/')
def all_notes():
    stmt = db.select(Note)
    notes = db.session.scalars(stmt)
    return NoteSchema(many=True).dump(notes)


@notes_bp.route('/', methods=['POST'])
@jwt_required()
def create_note():
    note_info = NoteSchema().load(request.json)
    stmt = db.select(Cat).filter_by(
        id=note_info.get('cat_id'))
    owner_id = db.session.scalar(stmt).owner_id
    admin_or_owner_required(owner_id)
    note = Note(
        message=note_info['message'],
        date_created=date.today(),
        # edit this if validating in schema
        is_negative=note_info.get('is_negative', False),
        cat_id=note_info['cat_id'],
        food_id=note_info['food_id']
    )
    db.session.add(note)
    db.session.commit()
    return NoteSchema().dump(note), 201


@notes_bp.route('/<int:note_id>')
def get_one_cat(note_id):
    stmt = db.select(Note).filter_by(id=note_id)
    note = db.session.scalar(stmt)
    if note:
        return NoteSchema().dump(note)
    else:
        return {'error': 'Note not found'}, 404


@notes_bp.route('/<int:note_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_note(note_id):
    note_info = NoteSchema().load(request.json)
    stmt = db.select(Note).filter_by(id=note_id)
    note = db.session.scalar(stmt)
    if note:
        owner_id = note.cat.owner_id
        admin_or_owner_required(owner_id)
        note.message = note_info.get('message', note.message)
        note.is_negative = note_info.get('is_negative', note.is_negative)
        note.cat_id = note_info.get('cat_id', note.cat_id)
        note.food_id = note_info.get('food_id', note.food_id)
        db.session.commit()
        return NoteSchema().dump(note)
    else:
        return {'error': 'Note not found'}, 404


@notes_bp.route('/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note(note_id):
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
