import os
from flask_restful import Resource


class ApiInfoResource(Resource):
    def get(self):

        return {"FLASK_APP": os.getenv("FLASK_APP"),
                "FLASK_ENV": os.getenv("FLASK_ENV"),
                "DEBUG": os.getenv("DEBUG")}

