from flask import request
from flask_restx import Namespace, Resource

from project.container import movie_service
from project.dao.models.movie import MovieSchema

movie_ns = Namespace("movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

#todo доделать вьюшки
@movie_ns.route("/")
class MoviesView(Resource):

    def get(self):
        """Get all movies"""
        movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    def post(self):
        """create new movie"""
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route("/<int:fid>")
class MovieView(Resource):

    def get(self, fid):
        """get movie by id"""
        movie = movie_service.get_one(fid)
        return movie_schema.dump(movie)

    def put(self, fid):
        """update movie by id"""
        req_json = request.json
        pass

    def delete(self, fid):
        """delete movie by id"""
        pass

