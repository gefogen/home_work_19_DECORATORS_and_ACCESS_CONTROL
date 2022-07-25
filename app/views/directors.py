from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.directors import Director, DirectorSchema
from app.setup_db import db
from app.container import director_service      # Импорт

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        director = director_service.get_all()
        return directors_schema.dump(director), 200

    def post(self):
        data = request.json
        new_movie = director_service.create(data)

        return "", 201


@director_ns.route('/<int:pk>')
class DirectorView(Resource):
    def get(self, pk):
        return director_schema.dump(director_service.get_one(pk))

    def put(self, pk):
        data = request.json
        director_service.update(pk, data)

        return "", 204

    def delete(self, pk):
        director_service.delete(pk)

        return "", 204