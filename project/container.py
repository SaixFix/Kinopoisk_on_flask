from project.dao import GenresDAO, DirectorDAO, MovieDAO, UserDAO

from project.services import GenresService
from project.services.director_service import DirectorService
from project.services.movie_service import MovieService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MovieDAO(db.session)
director_dao = DirectorDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
director_service = DirectorService(dao=director_dao)


