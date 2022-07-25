# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace

from app.decorators import auth_required, admin_required
from app.dao.model.movies import Movie, MovieSchema
from app.setup_db import db
from app.container import movie_service     # Импорт

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        year = request.args.get("year", type=int)

        movies = movie_service.get_all(
            {
            "director_id": director_id,
            "genre_id": genre_id,
            "year": year
            }
        )

        return movies_schema.dump(movies), 200

    @admin_required
    def post(self):
        data = request.json
        new_movie = movie_service.create(data)

        return "", 201, {'location': f"/movies/{new_movie.id}"}


@movie_ns.route('/<int:pk>')
class MovieView(Resource):
    @auth_required
    def get(self, pk):
        return movie_schema.dump(movie_service.get_one(pk)), 200

    @admin_required
    def put(self, pk):
        data = request.json
        movie_service.update(pk, data)

        return "", 204

    @admin_required
    def delete(self, pk):
        movie_service.delete(pk)

        return "", 204







