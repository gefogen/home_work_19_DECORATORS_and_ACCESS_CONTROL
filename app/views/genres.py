from flask import request
from flask_restx import Resource, Namespace

from app.decorators import auth_required, admin_required
from app.dao.model.genres import Genre, GenreSchema
from app.setup_db import db
from app.container import director_service, genre_service       # Импорт

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        genre = genre_service.get_all()
        return genres_schema.dump(genre), 200

    @admin_required
    def post(self):
        data = request.json
        new_movie = genre_service.create(data)

        return "", 201


@genre_ns.route('/<int:pk>')
class GenreView(Resource):
    @auth_required
    def get(self, pk):
        return genre_schema.dump(genre_service.get_one(pk))

    @admin_required
    def put(self, pk):
        data = request.json
        genre_service.update(pk, data)

        return "", 204

    @admin_required
    def delete(self, pk):
        genre_service.delete(pk)

        return "", 204