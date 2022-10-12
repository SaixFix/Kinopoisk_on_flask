from flask import request
from flask_restx import Namespace, Resource

from project.dao.models.movie import MovieSchema

movie_ns = Namespace("movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

#todo доделать вьюшки
@movie_ns.route("/")
class MoviesView(Resource):

    def get(self):
        """Get all movies"""
        pass

    def post(self):
        """create new movie"""
        req_json = request.json
        pass


@movie_ns.route("/<int:fid>")
class MovieView(Resource):

    def get(self, fid):
        """get movie by id"""
        pass

    def put(self, fid):
        """update movie by id"""
        req_json = request.json
        pass

    def delete(self, fid):
        """delete movie by id"""
        pass

