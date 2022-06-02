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
    def get(self):
        return '''<h1>Recommendation system of books</h1>
            <p>Item-based Collaborative filtration</p>'''

@api.route('/similarity')
class BookSimilarity(Resource):
    def get(self):
        amount = calculate_similarity()
        return jsonify({
                'status': '200 OK',
                'message':'Data is posted to MongoDB!',
                'amount': amount
            })

@api.route('/book/<string:id>')
class RecommendationByBook(Resource):
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