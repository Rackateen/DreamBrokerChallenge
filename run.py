from flask import Flask

my_app = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    my_app.run()
