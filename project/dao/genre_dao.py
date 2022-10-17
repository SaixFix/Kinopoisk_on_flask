from project.dao.base import BaseDAO
from project.dao.models.genre import Genre


class GenreDAO(BaseDAO[Genre]):
    __model__ = Genre

    def __init__(self, session):
        """Получает сессию"""
        self.session = session

    def create(self, data: dict):
        """Создаем новый жанр"""
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()

    def update(self, data: dict):
        """Обновляем данные жанра"""
        self.session.add(data)
        self.session.commit()

    def delete(self, did):
        """Удаляем жанр по id"""
        genre = self.get_one(did)
        self.session.delete(genre)
        self.session.commit()
