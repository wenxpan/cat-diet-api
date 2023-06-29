from flask import Blueprint, request
from init import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.cat import Cat, CatSchema
from models.food import Food, FoodSchema
from models.note import Note
from utils.authorise import admin_or_owner_required


# create blueprint for the /cats endpoint
cats_bp = Blueprint('cat', __name__, url_prefix='/cats')


@cats_bp.route('/')
def all_cats():
    # returns a list of cats and their owner name

    # build query: select all cats from cats table
    stmt = db.select(Cat)
    # execute query and return scalars result
    cats = db.session.scalars(stmt)

    # return serialized result
    return CatSchema(many=True, exclude=['owner_id', 'notes']).dump(cats)


@cats_bp.route('/', methods=['POST'])
@jwt_required()
def create_cat():
    # create a new cat in the database

    # load data using schema to sanitize and validate input
    cat_info = CatSchema().load(request.json, partial=True)

    # create a new Cat model instance
    cat = Cat(
        name=cat_info['name'],
        year_born=cat_info.get('year_born'), # optional
        year_adopted=cat_info.get('year_adopted'), # optional
        breed=cat_info.get('breed'), # optional
        owner_id=get_jwt_identity() # auto set from token identity
    )

    # add and commit cat to db
    db.session.add(cat)
    db.session.commit()

    # return serialized result
    return CatSchema(exclude=['owner_id', 'notes']).dump(cat), 201


@cats_bp.route('/<int:cat_id>')
def get_one_cat(cat_id):
    # returns cat of the selected id and their owner and notes

    # build query: select food with matching id
    stmt = db.select(Cat).filter_by(id=cat_id)
    # execute query and return a scalar result
    cat = db.session.scalar(stmt)
    if cat:
        # return seraialized result
        return CatSchema(exclude=['owner_id']).dump(cat)
    else:
        # if no cat is retrieved from db, return error
        return {'error': 'Cat not found'}, 404


@cats_bp.route('/<int:cat_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_cat(cat_id):
    # update cat information of the selected id

    # build query: select cat with matching id
    stmt = db.select(Cat).filter_by(id=cat_id)
    # execute query and return a scalar result
    cat = db.session.scalar(stmt)
    if cat:
        # check if token user is the cat owner
        admin_or_owner_required(cat.owner.id)

        # load data using schema to sanitize and validate input
        cat_info = CatSchema().load(request.json, partial=True)

        # update fields; all fields can be optional, so get methods are used
        cat.year_born = cat_info.get('year_born', cat.year_born)
        cat.year_adopted = cat_info.get('year_adopted', cat.year_adopted)
        # if not both fields are updated, marshmallow is unable to validate year logic
        # compare the latest values and return error when year_born is later than year_adopted
        if (not (cat_info.get('year_born') and cat_info.get(
            'year_adopted'))) and cat.year_born > cat.year_adopted:
            return {'error': 'year_adopted must be the same or later than year_born'}, 400
        
        # update remaining fields
        cat.name = cat_info.get('name', cat.name)
        cat.breed = cat_info.get('breed', cat.breed)

        # commit changes to db
        db.session.commit()

        # return updated cat
        return CatSchema(exclude=['owner_id', 'notes']).dump(cat)
    else:
        # if no cat is retrieved from db, return error
        return {'error': 'Cat not found'}, 404


@cats_bp.route('/<int:cat_id>', methods=['DELETE'])
@jwt_required()
def delete_cat(cat_id):
    # allows admin or owner to delete a cat from database

    # build query: select cat with matching id
    stmt = db.select(Cat).filter_by(id=cat_id)
    # execute query and return a scalar result
    cat = db.session.scalar(stmt)
    if cat:
        # check if the token user is the cat owner
        admin_or_owner_required(cat.owner.id)

        # delete cat instance and commit changes to db
        db.session.delete(cat)
        db.session.commit()
        # return success message
        return {'message': f"Cat {cat_id} and related notes deleted"}, 200
    else:
        # if no cat is retrieved from db, return error
        return {'error': 'Cat not found'}, 404


@cats_bp.route('/<int:cat_id>/food')
@jwt_required()
def get_cat_food(cat_id):
    # returns a list of foods tried by the cat, with statistics on total notes and rating
    
    # build query: select food instance, total count of notes, and total rating scores of notes
    # from joined table: notes JOIN foods, with filter that the note's cat_id matches the id in the request
    # grouped by foods, ordered by total rating scores in descending order
    stmt = db.select(Food, db.func.count(), db.func.sum(
        Note.rating)).select_from(Note).join(Food.notes).filter(
        Note.cat_id == cat_id).group_by(Food.id).order_by(db.func.sum(Note.rating).desc())
    
    # execute the query, get an iterable result of all the foods related to the selected cat, 
    # and the total notes reviewed, total rating scores for each related food, 
    # ranked from most to least positive reviewed
    statistics_info = db.session.execute(stmt)
    result = []

    # iterate through info and add statistics to result
    for food, count, rating in statistics_info:
        result.append({
            'food': FoodSchema(exclude=['notes']).dump(food),
            'total_notes': count,
            'total_rating': rating
        })
    return result