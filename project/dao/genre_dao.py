from project.dao.models.genre import Genre


class GenreDAO:

    def __init__(self, session):
        """Получает сессию"""
        self.session = session

    def get_all(self) -> list[dict]:
        """Возвращает все жанры"""
        return self.session.query(Genre).all()

    def get_one(self, did):
        """Возвращает жанр по id"""
        return self.session.query(Genre).get(did)

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
