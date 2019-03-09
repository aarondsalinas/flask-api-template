from flask import Flask
from api.main.resources import api

app = Flask(__name__)
api.init_app(app)

def run():
    app.run()


if __name__ == '__main__':
    run()

