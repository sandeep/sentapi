import sys, getopt;
import pattern;

from pattern.en import sentiment
from nltk.sentiment import SentimentIntensityAnalyzer

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('text', type=str, help='Text Blob for sentiment analysis')

class Sentiment(Resource):
	def post(self):
		args = parser.parse_args()
		q= sentiment(str(args['text']))
		print q
		return {'sentiment': q}

api.add_resource(Sentiment, '/')

if __name__ == '__main__':
	app.run(debug=True)
