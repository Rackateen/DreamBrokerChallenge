from flask import Flask, jsonify, request
#from collections import Counter
import json

my_app = Flask(__name__)


@my_app.route('/', methods=['GET', 'POST'])
def index():
	if (request.method == 'POST'):
		#format output python dict
		final = dict()
		#get the request data
		some_json = request.get_json()
		text = some_json["text"]

		#churn through data
		textLength = {"withSpaces": len(text), "withoutSpaces": (len(text) - text.count(' '))}
		final["textLength"] = textLength
		final["WordCount"] = len(text.split())
		#final["characterCount"] = Counter(text)
		characterCount = []
		tempCharDict = dict()
		tempText = ''.join(sorted(text.lower()))
		for i in tempText:
			tempCharDict[i] = text.count(i)
			if i.isalpha() and not tempCharDict in characterCount:
				characterCount.append(tempCharDict.copy())
			tempCharDict = dict()
		
		final["characterCount"] = characterCount
		return json.dumps(final), 201
	else:
    		return "Welcome to Lewis' magic API"


if __name__ == '__main__':
	my_app.run(debug=true)
