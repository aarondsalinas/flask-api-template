from flask import Blueprint
from flask_restplus import Api
from .healthResource import api as health_resource_ns

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint,
          title='API',
          version='1.0',
          description='Flask RestPlus API Template'
          )

api.add_namespace(health_resource_ns, path='/health')
