from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS
from bson.objectid import ObjectId
from flask_restx import Api, Resource

from config import *
from calculation_bll import *

app = Flask(__name__)
api = Api(app)

client = MongoClient(connectionString)
db = client['masters']
CORS(app)

connect_to_database(db)

@api.route('/')
class Home(Resource):
    """
    Home endpoint with general info.

    :param Resource: abstract RESTX resource for Flask API
    :returns: home page with general description
    """

    def get(self):
        return '''<h1>Recommendation system of books</h1>
            <p>Item-based Collaborative filtration</p>'''

@api.route('/similarity')
class BookSimilarity(Resource):
    """
    Endpoint that runs the similarity collection update

    :param Resource: abstract RESTX resource for Flask API
    :returns: amount of records saved in MongoDB 
    """

    def get(self):
        amount = calculate_similarity()
        return jsonify({
                'status': '200 OK',
                'message':'Data is saved in MongoDB!',
                'amount': amount
            })

@api.route('/book/<string:id>')
class RecommendationByBook(Resource):
    """
    Endpoint that generates recommendation based on book

    :param Resource: abstract RESTX resource for Flask API
    :param id: id of the book for which there is a need to find similar items 
    :returns: home page with general description
    """

    def get(self, id):
        recommedations = []
        bookd_id = ObjectId(id) # 620ea6721feee707fc54939a - id for testing
        for item in calculate_recomendations_by_book(bookd_id):
            recommedations.append({
                'rate': item[0],
                'bookId': str(item[1])
            })
        return jsonify(recommedations)

@api.route('/user/<string:id>')
class RecommendationForUser(Resource):
    """
    Endpoint that generates recommendation for a particular user

    :param Resource: abstract RESTX resource for Flask API
    :param id: id of the user for whom there is a need to generate recommendations
    :returns: home page with general description
    """

    def get(self, id):
        recommedations = []
        user_id = ObjectId(id) # 620bb9fef23b1bc78052c605 - id for testing
        for item in calculate_recomendations_for_user(user_id):
            recommedations.append({
                'rate': item[0],
                'bookId': str(item[1])
            })
        return jsonify(recommedations)

if __name__ == '__main__':
    app.run(debug = True)