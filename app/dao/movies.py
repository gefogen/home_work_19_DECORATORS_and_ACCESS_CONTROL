# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from app.dao.model.movies import Movie, MovieSchema
from app.setup_db import db     # Импорт


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        if filters.get('director_id'):
            movies = Movie.query.filter(Movie.director_id == filters.get('director_id')).all()
            return movies

        if filters.get('genre_id'):
            genres = Movie.query.filter(Movie.genre_id == filters.get('genre_id')).all()
            return genres

        if filters.get('year'):
            year = Movie.query.filter(Movie.year == filters.get('year')).all()
            return year

        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get_or_404(mid)

    def create(self, data):
        new_movie = Movie(**data)

        db.session.add(new_movie)
        db.session.commit()

        return new_movie


    def update(self, mid, data):
        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        db.session.add(movie)
        db.session.commit()


    def delete(self, mid):
        movie = self.get_one(mid)

        db.session.delete(movie)
        db.session.commit()
