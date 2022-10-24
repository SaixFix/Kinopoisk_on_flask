from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссеры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Иванов'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Спартак'),
    'description': fields.String(required=True, max_length=100, example='Ор взял меч и пошёл сечь!'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/'),
    'year': fields.Integer(required=True, example=2008),
    'rating': fields.Float(required=True, example=7.1),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='fifa@pokpok.ru'),
    'password': fields.String(required=True, max_length=100, example='162548'),
    'name': fields.String(required=True, max_length=100, example='Vladimir'),
    'surname': fields.String(required=True, max_length=100, example='Volfovich'),
    'genre': fields.Nested(genre),
})