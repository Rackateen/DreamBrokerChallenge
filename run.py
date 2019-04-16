from flask import Flask, jsonify, request

my_app = Flask(__name__)


@my_app.route('/', methods=['GET', 'POST'])
def index():
	if (request.method == 'POST'):
		some_json = request.get_json()
		return jsonify({'you sent': some_json}), 201
	else:
    		return jsonify({"about":"Hello World!"})


if __name__ == '__main__':
    my_app.run()
