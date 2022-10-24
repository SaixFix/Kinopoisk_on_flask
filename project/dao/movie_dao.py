from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO
from project.dao.models.movie import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_order_by(self, page:int, filter:Optional[str]):
        stmt: BaseQuery = self._db_session.query(self.__model__) # select * from self model
        if filter:
            stmt = stmt.order_by(desc(self.__model__)) # order_by model.year desc
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()


