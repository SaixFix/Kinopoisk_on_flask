from project.dao.models.movie import Movie


class MovieDAO:

    def __init__(self, session):
        """Получает сессию"""
        self.session = session

    def get_all(self) -> list[dict]:
        """Возвращает все фильмы"""
        return self.session.query(Movie).all()

    def get_one(self, fid):
        """Возвращает фильм по id"""
        return self.session.query(Movie).get(fid)

    def create(self, data: dict):
        """Создаем новый фильм"""
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update(self, data: dict):
        """Обновляем данные фильма"""
        self.session.add(data)
        self.session.commit()

    def delete(self, fid):
        """Удаляем фильм по id"""
        movie = self.get_one(fid)
        self.session.delete(movie)
        self.session.commit()



