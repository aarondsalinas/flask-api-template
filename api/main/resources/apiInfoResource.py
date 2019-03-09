import os
from flask_restplus import Resource, Api
from app import api


@api.route('/info')
class ApiInfoResource(Resource):
    def get(self):
        return {"FLASK_APP": os.getenv("FLASK_APP"),
                "FLASK_ENV": os.getenv("FLASK_ENV"),
                "DEBUG": os.getenv("DEBUG")}


