from flask_restplus import Resource, Namespace

api = Namespace('healthResource', description="Health Resource")


@api.route('')
class HealthResource(Resource):
    def get(self):
        return "Success"

