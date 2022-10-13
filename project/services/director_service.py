from project.dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        """Получаем ДАО"""
        self.dao = dao

    def get_all(self) -> list[dict]:
        """Возвращает всех режиссеров"""
        return self.dao.get_all()

    def get_one(self, data: dict):
        """Возвращает режиссера по id"""
        return self.dao.get_one(data)

    def create(self, data: dict):
        """Создаем нового режиссера"""
        self.dao.create(data)

    def update(self, data: dict, did: int):
        """Обновляем данные режиссера"""
        director = self.get_one(did)

        if "name" in data:
            director.name = data.get("name")

    def delete(self, did):
        """Удаляем режиссера по id"""
        self.dao.delete(did)
