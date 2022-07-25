from app.dao.model.directors import Director, DirectorSchema
from app.setup_db import db     # Импорт


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def create(self, data):
        new_director = Director(**data)

        db.session.add(new_director)
        db.session.commit()

        return new_director

    def update(self, did, data):
        director = self.get_one(did)

        director.title = data.get('title')
        director.description = data.get('description')
        director.trailer = data.get('trailer')
        director.year = data.get('year')
        director.rating = data.get('rating')
        director.genre_id = data.get('genre_id')
        director.director_id = data.get('director_id')

        db.session.add(director)
        db.session.commit()


    def delete(self, did):
        director = self.get_one(did)

        db.session.delete(director)
        db.session.commit()