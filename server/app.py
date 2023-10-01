from flask import Flask,request,jsonify,session,make_response
from flask_migrate import Migrate
from flask_restful import Api,Resource


from models.config import db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import restaurant_pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza-restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



api = Api(app)
db.init_app(app)
migrate = Migrate(app,db)

class Display(Resource):
    def get(self):
        restaurants = [
            {'id':restaurant.id,
             'name':restaurant.name,
             'adress':restaurant.address
             } 
            for restaurant in Restaurant.query.all()
        ]
        return jsonify(restaurants)
    

class Display_Restaurants_by_id(Resource):
    def get(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        
        if not restaurant:
            return {'error':'Restaurant not Found'},401
        
        # return jsonify(restaurant),200
        # return restaurant
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizza':[
                {
                'id': pizza.id,
                'name':pizza.name,
                'ingredients':pizza.ingredients 
                }  
             for pizza in restaurant.pizza
            ]
        }
        
        return jsonify(restaurant_data)
    
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()

        if not restaurant:
            return {"error": "restaurant not found"},401
        
        db.session.delete(restaurant)
        db.session.commit()

        return {}, 200
    
             
class Display_Pizzas(Resource):
    def get(self):
        pizzas= [ 
            {
                'id':pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            } 
            for pizza in Pizza.query.all()

        ]

        return pizzas, 200
    


class CreateRestaurantPizza(Resource):
    def post(self):
        data = request.get_json()

        # Check if all required fields are present in the request data
        required_fields = ["price", "pizza_id", "restaurant_id"]
        if not all(field in data for field in required_fields):
            return ({"errors": ["price, pizza_id, and restaurant_id are required fields"]}), 400

        # Retrieve the pizza and restaurant by their IDs
        pizza = Pizza.query.get(data["pizza_id"])
        restaurant = Restaurant.query.get(data["restaurant_id"])
        
        

        # Check if both pizza and restaurant exist
        if not pizza or not restaurant:
            return {"error": "validation errors"}, 404

        # Create a new RestaurantPizza instance and add it to the session
        restaurant_pizza_association= restaurant_pizza.insert().values(
            price=data['price'],
            restaurant_id= data['restaurant_id'],
            pizza_id=data['pizza_id']
        )
        db.session.execute(restaurant_pizza_association)
        db.session.commit()

        # Return the pizza data associated with the created RestaurantPizza
        pizza_data = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }

        return (pizza_data), 201

# ... (existing code)

# Add the new resource for creating RestaurantPizza
api.add_resource(CreateRestaurantPizza, '/restaurant_pizzas', endpoint='/restaurant_pizzas')



        
api.add_resource(Display,'/restaurants',endpoint='/restaurants')
api.add_resource(Display_Restaurants_by_id,'/restaurants/<int:id>',endpoint='/restaurants/<int:id>')
api.add_resource(Display_Pizzas,'/pizzas', endpoint='/pizzas')

if __name__ == "__main__":
    app.run(port=5555,debug=True)