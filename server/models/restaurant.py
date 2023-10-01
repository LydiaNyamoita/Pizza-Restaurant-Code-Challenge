
from .config import db
from .restaurant_pizza import restaurant_pizza



class Restaurant(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    
    pizza = db.relationship('Pizza', secondary=restaurant_pizza, backref='restaurants')