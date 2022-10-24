from typing import Optional

from project.dao.base import BaseDAO
from project.dao.models.movie import Movie
from project.exceptions import ItemNotFound
from project.models import Genre



class MovieService:

    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, filter=None, page: Optional[int] = None) -> list[Movie]:
        return self.dao.get_all_order_by(page=page, filter=filter)