from flask import request
from flask_restx import Namespace, Resource

from project.container import genre_service
from project.dao.models.director import DirectorSchema
from project.setup.api.models import genre
from project.setup.api.parsers import page_parser

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


api = Namespace('genres')


@api.route('/')
class DirectorsView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(genre, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all genres.
        """
        return genre_service.get_all(**page_parser.parse_args())

    def post(self):
        """create new director"""
        req_json = request.json
        pass


@api.route('/<int:did>/')
class DirectorView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(genre, code=200, description='OK')
    def get(self, did: int):
        """
        Get genre by id.
        """
        return genre_service.get_item(did)