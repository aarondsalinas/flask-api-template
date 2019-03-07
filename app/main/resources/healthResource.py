from flask import Flask, Blueprint
from flask_restplus import Api, Resource

healthResource = Blueprint('healthResource', __name__)


@healthResource.route("/")
class HealthResource(Resource):
    @healthResource.doc('list_of_registered_users')
    def get(self):
        return "Success"
