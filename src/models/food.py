from init import db, ma


class Food(db.Model):
    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    name = db.Column(db.String, nullable=False, unique=True)
    brand = db.Column(db.String)


class FoodSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type', 'name', 'brand')
