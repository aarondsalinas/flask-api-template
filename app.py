from flask import Flask
from api.main.resources import blueprint as resource_bp

app = Flask(__name__)
app.register_blueprint(resource_bp)


def run():
    app.run()


if __name__ == '__main__':
    run()

