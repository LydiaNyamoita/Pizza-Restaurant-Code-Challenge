from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

 


restaurant_pizza = db.Table(
    'restaurant_pizza',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('price', db.Integer),
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'))
)



class Restaurant(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    
    pizza = db.relationship('Pizza', secondary=restaurant_pizza, backref='restaurants')

class Pizza(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
   
    

