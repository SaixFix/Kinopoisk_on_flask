from flask import request
from flask_restx import Namespace

api = Namespace('auth')

#todo дописать
@api.route("/register")
class AuthRegView:

    def post(self):
        """get user data and create new user"""
        pass

@api.route("/login ")
class AuthLoginView:

    def post(self):
        """get login and pass and return access and refresh tokens"""
        pass

    def put(self):
        """get pair tokens if they valid create new pairs"""
        pass
