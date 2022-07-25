from app.dao.genres import GenreDAO
from app.setup_db import db     # Импорт


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all(self):
        return self.genre_dao.get_all()

    def get_one(self, gid):
        return self.genre_dao.get_one(gid)

    def create(self, data):
        return self.genre_dao.create(data)

    def update(self, gid, data):
        return self.genre_dao.update(gid, data)

    def delete(self, gid):
        return self.genre_dao.delete(gid)