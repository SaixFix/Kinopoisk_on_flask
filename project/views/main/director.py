from flask import request
from flask_restx import Namespace, Resource

from project.dao.models.director import DirectorSchema

director_ns = Namespace("directors")

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorsView(Resource):

    def get(self):
        """get all directors"""
        pass

    def post(self):
        """create new director"""
        req_json = request.json
        pass


@director_ns.route("/<int:did>")
class DirectorView(Resource):

    def get(self, did):
        """get director by id"""
        pass

    def put(self, did):
        """update director bu id"""
        req_json = request.json
        pass
