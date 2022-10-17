from marshmallow import Schema, fields
from sqlalchemy import Column, String, ForeignKey

from project.dao.models.genre import Genre
from project.setup.db import models


class User(models):
    __tablename__ = "user"
    name = Column(String(100))
    surname = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(300), unique=True, nullable=False)
    favorite_genre = Column(String(50))


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String
    password = fields.String
    name = fields.String()
    surname = fields.String()
    favorite_genre = Column(ForeignKey(f"{Genre.__tablename__}.id"), nullable=False)

