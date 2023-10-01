from models import db, Restaurant, Pizza, restaurant_pizza
from app import app

with app.app_context():
    # Create some restaurants
    restaurant1 = Restaurant(name="Pizza Palace", address="123 Main St")
    restaurant2 = Restaurant(name="Mama Mia Pizzeria", address="456 Elm St")
    restaurant3 = Restaurant(name="Pepperoni Heaven", address="789 Oak St")

    # Create some pizzas
    pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    pizza3 = Pizza(name="Vegetarian", ingredients="Tomato, Mozzarella, Bell Peppers, Mushrooms")

    # Add data to the session
    db.session.add_all([restaurant1, restaurant2, restaurant3, pizza1, pizza2, pizza3])
    db.session.commit()  # Commit the data to get the restaurant and pizza IDs

    # Create associations between restaurants and pizzas in the restaurant_pizza association table
    restaurant_pizza1 = restaurant_pizza.insert().values(price=10.99, restaurant_id=restaurant1.id, pizza_id=pizza1.id)
    restaurant_pizza2 = restaurant_pizza.insert().values(price=12.99, restaurant_id=restaurant1.id, pizza_id=pizza2.id)
    restaurant_pizza3 = restaurant_pizza.insert().values(price=11.99, restaurant_id=restaurant2.id, pizza_id=pizza1.id)
    restaurant_pizza4 = restaurant_pizza.insert().values(price=13.99, restaurant_id=restaurant2.id, pizza_id=pizza3.id)
    restaurant_pizza5 = restaurant_pizza.insert().values(price=11.49, restaurant_id=restaurant3.id, pizza_id=pizza2.id)

    # Add association data to the session and commit
    db.session.execute(restaurant_pizza1)
    db.session.execute(restaurant_pizza2)
    db.session.execute(restaurant_pizza3)
    db.session.execute(restaurant_pizza4)
    db.session.execute(restaurant_pizza5)
    db.session.commit()

    print("Seed data has been added to the database.")
