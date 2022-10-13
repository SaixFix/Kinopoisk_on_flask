class MovieService:

    def __init__(self, dao):
        """Получает сессию"""
        self.dao = dao

    def get_all(self) -> list[dict]:
        """Возвращает все фильмы"""
        return self.dao.get_all()

    def get_one(self, fid: int) -> dict:
        """Возвращает фильм по id"""
        return self.dao.get_one(fid)

    def create(self, data: dict):
        """Создаем новый фильм"""
        return self.dao.create(data)

    def update(self, data: dict):
        """Обновляем данные фильма"""
        self.session.add(data)
        self.session.commit()

    def delete(self, fid):
        """Удаляем фильм по id"""
        movie = self.get_one(fid)
        self.session.delete(movie)
        self.session.commit()
