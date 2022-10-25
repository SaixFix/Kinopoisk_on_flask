from flask import request
from flask_restx import Namespace, Resource

from project.container import genre_service, director_service
from project.setup.api.models import genre, director
from project.setup.api.parsers import page_parser


api = Namespace('directors')


@api.route('/')
class DirectorsView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all genres.
        """
        return director_service.get_all(**page_parser.parse_args())


@api.route('/<int:did>/')
class DirectorView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(genre, code=200, description='OK')
    def get(self, did: int):
        """
        Get genre by id.
        """
        return genre_service.get_item(did)