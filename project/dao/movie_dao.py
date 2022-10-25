from typing import Optional

from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO
from project.models import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_order_by(self, page, filter):
        """Функция выводит список фильмов по странично(если задано на входе) и с фильтрацией по году(если фильтр задан на входе)"""
        stmt = self._db_session.query(self.__model__)  # select * from self model
        if filter == 'new':
            stmt = stmt.order_by(desc(self.__model__.year))  # order_by model.year desc
        if filter == 'old':
            stmt = stmt.order_by(self.__model__.year) # order_by model.year desc
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()
