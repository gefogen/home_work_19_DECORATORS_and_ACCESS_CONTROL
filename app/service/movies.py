# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model


# Пример
from app.dao.movies import MovieDAO
from app.setup_db import db     # Импорт


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all(self, filters: dict):
        return self.movie_dao.get_all(filters)

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def create(self, data):
        return self.movie_dao.create(data)

    def update(self, mid, data):
        return self.movie_dao.update(mid, data)

    def delete(self, mid):
        return self.movie_dao.delete(mid)