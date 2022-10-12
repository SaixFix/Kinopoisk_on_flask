from project.dao.models.director import Director


class DirectorDAO:

    def __init__(self, session):
        """Получает сессию"""
        self.session = session

    def get_all(self) -> list[dict]:
        """Возвращает всех режиссеров"""
        return self.session.query(Director).all()

    def get_one(self, did):
        """Возвращает фильм по id"""
        return self.session.query(Director).get(did)

    def create(self, data: dict):
        """Создаем нового режиссера"""
        director = Director(**data)
        self.session.add(director)
        self.session.commit()

    def update(self, data: dict):
        """Обновляем данные режиссера"""
        self.session.add(data)
        self.session.commit()

    def delete(self, did):
        """Удаляем режиссера по id"""
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()
