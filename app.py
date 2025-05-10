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
        new_production = Production(**data)
        # Validate the data (you can add more validation as needed)
        
        # Add the new production to the database 
        db.session.add(new_production)
        db.session.commit()

        # Serialize the new production and return a success response
        return make_response(jsonify({
            'message': 'Production created successfully!',
            'production': new_production.to_dict()
        }), 201)

api.add_resource(Productions, '/api/productions')

class ProductionById(Resource):
    def get(self, production_id):
        # Query the database to get a specific Production record by ID
        production = Production.query.get_or_404(production_id)
        return make_response(jsonify({'production': production.to_dict()}), 200)

    def put(self, production_id):
        # Get the JSON data from the request
        data = request.get_json()

        # Query the database to get the Production record by ID
        production = Production.query.get_or_404(production_id)

        # Update the production with new data
        for key, value in data.items():
            setattr(production, key, value)

        db.session.commit()

        return make_response(jsonify({
            'message': 'Production updated successfully!',
            'production': production.to_dict()
        }), 200)

    def delete(self, production_id):
        # Query the database to get the Production record by ID
        production = Production.query.filter_by(id=production_id).first_or_404()

        # Delete the production from the database
        db.session.delete(production)
        db.session.commit()

        return make_response(jsonify({'message': 'Production deleted successfully!'}), 200)

api.add_resource(ProductionById, '/api/productions/<int:production_id>')
