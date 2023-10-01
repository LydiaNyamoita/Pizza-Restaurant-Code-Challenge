from .config import db


restaurant_pizza = db.Table(
    'restaurant_pizza',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('price', db.Integer),
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'))
)