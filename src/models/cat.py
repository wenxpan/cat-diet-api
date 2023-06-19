from init import db, ma


class Cat(db.Model):
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    year_born = db.Column(db.String)
    year_adopted = db.Column(db.String)
    breed = db.Column(db.String)


class CatSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'year_born', 'year_adopted')
