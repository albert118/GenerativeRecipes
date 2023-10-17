from flask_injector import inject
from infrastructure.ModelProvider import ModelProvider
from configuration import ApiNamespace
from flask_restx import Resource

ns = ApiNamespace()

@inject
@ns.route('<prompt:string>')
@ns.response(200, 'OK')
@ns.param('prompt', 'A prompt for a new image')
class Image(Resource):
    ''''''
    def __init__(self):
        self.model_provider = ModelProvider()

    @ns.doc('get_image')
    def get(self):
        '''Get a new image'''
        return self.model_provider.do_thing()
