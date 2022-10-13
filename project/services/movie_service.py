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

    def update(self, data: dict, fid: int):
        """Обновляем данные фильма"""
        movie = self.get_one(fid)
        if "title" in data:
            movie.title = data.get("title")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "year" in data:
            movie.year = data.get("year")
        if "rating" in data:
            movie.rating = data.get("rating")
        if "genre_id" in data:
            movie.title = data.get("genre_id")
        if "director_id" in data:
            movie.title = data.get("director_id")

        self.dao.update(movie)

    def delete(self, fid):
        """Удаляем фильм по id"""
        self.dao.delete(fid)
