import sys, getopt;
import pattern;

from pattern.en import sentiment
from nltk.sentiment import SentimentIntensityAnalyzer
from pattern.en import parse

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('text', type=str, help='Requires text attribute. Returns a polarity, subjectivity score for the given sentence, based on the adjectives it contains, where polarity is a value between -1.0 and +1.0 and subjectivity between 0.0 and 1.0. ')
parser.add_argument('messages', type = list, location='json')

class Sentiment(Resource):
	def get(self):
		args = parser.parse_args()

		return

	def post(self):
		args = parser.parse_args()
		output = []
		if args['messages']:
			messages =  args['messages']
		else:
				#we should sanitize this.
			messages = [{"text": args['text'],"id": ''}]

		for message in messages:
			print message
			messageSentiment = sentiment(str(message["text"]))
			output.append({'sentiment':
			{
			'polarity': messageSentiment[0],
			'subjectivity': messageSentiment[1]
			},
			'id': message["id"]
			})


		return {'sentiments':output}

api.add_resource(Sentiment, '/')

if __name__ == '__main__':
	app.run(debug=True)
