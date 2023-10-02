from .config import db
from sqlalchemy import CheckConstraint

restaurant_pizza = db.Table(
    'restaurant_pizza',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('price', db.Integer, nullable=False),
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id')),
    CheckConstraint('price >= 1 AND price <= 30', name='price_range')  
)
