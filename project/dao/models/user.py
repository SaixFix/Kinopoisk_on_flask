from marshmallow import Schema, fields

from project.setup.db import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    favorite_genre = db.Column(db.String(50))


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String
    password = fields.String
    name = fields.String()
    surname = fields.String()
    favorite_genre = fields.String()

