from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.users import User, UserSchema
from app.setup_db import db
from app.container import user_service  # Импорт

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        users = user_service.get_all()

        return users_schema.dump(users), 200

    def post(self):
        data = request.json
        new_user = user_service.create(data)

        return "", 201, {'location': f"/users/{new_user.id}"}


@user_ns.route('/<int:pk>')
class UserView(Resource):
    def get(self, pk):
        return user_schema.dump(user_service.get_one(pk)), 200

    def put(self, pk):
        data = request.json
        user_service.update(pk, data)

        return "", 204

    def delete(self, pk):
        user_service.delete(pk)

        return "", 204
