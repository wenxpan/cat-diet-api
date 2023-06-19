from init import db, ma


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    date_created = db.Column(db.Date)
    is_negative = db.Column(db.Boolean, default=False)
    # cat_id
    # food_id


class NoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'message', 'date_created', 'is_negative')
