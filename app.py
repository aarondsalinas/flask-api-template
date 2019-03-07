from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


def run():
    app.run()


if __name__ == '__main__':
    run()

