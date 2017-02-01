import sys, getopt;
import pattern;

from pattern.en import sentiment
from nltk.sentiment import SentimentIntensityAnalyzer

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('text', required =True, type=str, help='Requires text attribute. Returns a polarity, subjectivity score for the given sentence, based on the adjectives it contains, where polarity is a value between -1.0 and +1.0 and subjectivity between 0.0 and 1.0. ')

class Sentiment(Resource):
	def get(self):
		args = parser.parse_args()

		return

	def post(self):
		args = parser.parse_args()
		#we should sanitize this.
		messageSentiment = sentiment(str(args['text']))

		print messageSentiment[0]
		return {'sentiment':
		{
			'polarity': messageSentiment[0],
			'subjectivity': messageSentiment[1]
		}
		}

api.add_resource(Sentiment, '/')

if __name__ == '__main__':
	app.run(debug=True)
