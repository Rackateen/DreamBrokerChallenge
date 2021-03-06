from flask import Flask, jsonify, request
import json
#By Lewis Torrington, 17.04.2019

my_app = Flask(__name__)

@my_app.route('/', methods=['GET', 'POST'])
def index():
	if (request.method == 'POST'):
		#test whether the data is valid
		if not request.content_type == 'application/json':
       			return 'Content-type must be application/json', 401	
		
		#format output python dict
		final = dict()
		
		#get the request data
		some_json = request.get_json()
		if not "text" in some_json:
			return 'JSON sent must be text', 401
		text = some_json["text"]

		#churn through data
		textLength = {"withSpaces": len(text), "withoutSpaces": (len(text) - text.count(' '))}
		final["textLength"] = textLength
		final["wordCount"] = len(text.split())
		characterCount = []
		tempCharDict = dict()
		tempText = ''.join(sorted(text.lower()))
		for i in tempText:
			tempCharDict[i] = tempText.count(i)
			if i.isalpha() and not tempCharDict in characterCount:
				characterCount.append(tempCharDict.copy())
			tempCharDict = dict()
		final["characterCount"] = characterCount
		return json.dumps(final)
	else:
    		return "Welcome to Lewis' magic API"


if __name__ == '__main__':
	my_app.run(debug=true)
