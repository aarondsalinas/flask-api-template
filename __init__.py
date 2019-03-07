from flask import Flask
from app.main.resources import bp as health_bp

app = Flask(__name__)

app.register_blueprint(health_bp, url_prefix='/health')