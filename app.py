import os
from flask_restful import Api
from . import create_app
from api.main.resources.healthResource import HealthResource
from api.main.resources.apiInfoResource import ApiInfoResource

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()

api = Api(app)
api.add_resource(HealthResource, "/health")
api.add_resource(ApiInfoResource, "/info")


def run():
    app.run()


if __name__ == '__main__':
    run()

