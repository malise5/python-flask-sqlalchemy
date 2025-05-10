from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate, migrate
# from models import db, Production
from flask_restful import Api, Resource

from models import db, Production



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False  # Disable compact JSON for better readability
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # Enable pretty print for JSON responses


migrate = Migrate(app, db)
db.init_app(app)

# Initialize Flask-Restful API
api = Api(app)

# Define a resource for the Production model
class Productions(Resource):
    def get(self):
        # Query the database to get all Production records
        productions = Production.query.all()
        production_list = [p.to_dict() for p in productions]
        return make_response(jsonify({'productions': production_list}), 200)
    

    def post(self):
        # Get the JSON data from the request
        data = request.get_json()

        # Create a new Production instance
        new_production = Production(
            title=data['title'],
            genre=data['genre'],
            budget=data['budget'],
            imageUrl=data['imageUrl'],
            director=data['director'],
            description=data['description']
        )
        
        # Add the new production to the database 
        db.session.add(new_production)
        db.session.commit()
        
        return make_response(jsonify({'message': 'Production created successfully!'}), 201)

api.add_resource(Productions, '/api/productions')
