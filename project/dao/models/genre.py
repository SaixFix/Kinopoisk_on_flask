from marshmallow import Schema, fields

from project.setup.db import db


class Director(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)  # todo присвоить уникальность


class DirectorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()