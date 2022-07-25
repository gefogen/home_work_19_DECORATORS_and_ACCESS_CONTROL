from app.dao.directors import DirectorDAO
from app.setup_db import db  # Импорт


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_all(self):
        return self.director_dao.get_all()

    def get_one(self, did):
        return self.director_dao.get_one(did)

    def create(self, data):
        return self.director_dao.create(data)

    def update(self, did, data):
        return self.director_dao.update(did, data)

    def delete(self, did):
        return self.director_dao.delete(did)
