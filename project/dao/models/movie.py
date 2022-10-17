from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.dao.models.director import Director
from project.dao.models.genre import Genre
from project.setup.db import models


class Movie(models):
    __tablename__ = "movie"
    title = Column(String(100))
    trailer = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(ForeignKey(f"{Genre.__tablename__}.id"), nullable=False)
    genre = relationship("Genre")
    director_id = Column(ForeignKey(f"{Director.__tablename__}.id"), nullable=False)
    director = relationship("Director")


class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    genre_id = fields.Pluck("GenreSchema", "name")
    director_id = fields.Pluck("DirectorSchema", "name")

