from flask import Flask, jsonify, request
import json

my_app = Flask(__name__)


@my_app.route('/', methods=['GET', 'POST'])
def index():
	if (request.method == 'POST'):
		#format output python dict
		final = {
		"textLength": "",
		"WordCount": 0,
		"characterCount": ""
		}
		#get the request data
		some_json = request.get_json()
		text = some_json["text"]

		#churn through data
		textLength = {"withSpaces": len(text), "withoutSpaces": (len(text) - text.count(' '))}
		final["WordCount"] = len(text.split())		
		
		return json.dumps(final), 201
	else:
    		return "Welcome to Lewis' magic API"


if __name__ == '__main__':
	my_app.run(debug=true)
