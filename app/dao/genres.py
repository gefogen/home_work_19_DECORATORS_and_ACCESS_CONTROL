from app.dao.model.genres import Genre, GenreSchema
from app.setup_db import db     # Импорт


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def create(self, data):
        new_genre = Genre(**data)

        db.session.add(new_genre)
        db.session.commit()

        return new_genre

    def update(self, gid, data):
        genre = self.get_one(gid)

        genre.title = data.get('title')
        genre.description = data.get('description')
        genre.trailer = data.get('trailer')
        genre.year = data.get('year')
        genre.rating = data.get('rating')
        genre.genre_id = data.get('genre_id')
        genre.genre_id = data.get('genre_id')

        db.session.add(genre)
        db.session.commit()


    def delete(self, gid):
        genre = self.get_one(gid)

        db.session.delete(genre)
        db.session.commit()