from flask_restplus import Api
from .healthResource import api as health_resource_ns

api = Api(
    title='API',
    version='1.0',
    description='Flask RestPlus API Template',
    prefix='/api'
)

api.add_namespace(health_resource_ns, path='/health')