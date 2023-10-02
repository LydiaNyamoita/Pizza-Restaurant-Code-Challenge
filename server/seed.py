import random
from app import app
from models.config import db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import restaurant_pizza

with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()
    db.session.commit()

  
    restaurants = [
        Restaurant(name="Pizza Palace", address="123 Main St"),
        Restaurant(name="Mama Mia Pizzeria", address="456 Elm St"),
        Restaurant(name="Pepperoni Heaven", address="789 Oak St")
    ]

    
    pizzas = [
        Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil"),
        Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni"),
        Pizza(name="Vegetarian", ingredients="Tomato, Mozzarella, Bell Peppers, Mushrooms")
    ]

    
    db.session.add_all(restaurants + pizzas)
    db.session.commit() 

    
    restaurant_pizza_data = []

    for _ in range(6):  
        for restaurant in restaurants:
            for pizza in pizzas:
                price = random.randint(1, 30)  
                association = {
                    "price": price,
                    "restaurant_id": restaurant.id,
                    "pizza_id": pizza.id
                }
                restaurant_pizza_data.append(association)

    
    db.session.execute(restaurant_pizza.insert().values(restaurant_pizza_data))
    db.session.commit()

    print("Seed data has been added to the database.")
