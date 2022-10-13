from marshmallow import Schema, fields

from project.setup.db import db


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    genre_id = fields.Pluck("GenreSchema", "name")
    director_id = fields.Pluck("DirectorSchema", "name")

