from flask_restx import Namespace

api = Namespace('user')

#todo доделать
@api.route("/")
class UserView:

    def get(self):
        """get user's infomation"""

    def patch(self):
        """change information user"""


@api.route("/password")
class UserPassView:

    def put(self, password):
        """get old password and new then change password"""
