from urllib import response
from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate, migrate
from models import db, Production


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)




@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/productions', methods=['GET'])
def get_productions():
    # This is where you would normally query the database for productions
    # I have imported the Production model from models.py
    productions = Production.query.all()
    response = []