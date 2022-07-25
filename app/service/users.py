import base64
import hashlib

from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS  # Метод хеширование пароля
from app.dao.users import UserDAO
from app.setup_db import db     # Импорт


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_all(self, filters: dict):
        return self.user_dao.get_all(filters)

    def get_one(self, uid):
        return self.user_dao.get_one(uid)

    def get_by_username(self, uid):
        return self.user_dao.get_by_username(uid)

    def create(self, data):
        data["password"] = self.generate_password(data["password"])
        return self.user_dao.create(data)

    def update(self, uid, data):
        data["password"] = self.generate_password(data["password"])
        return self.user_dao.update(uid, data)

    def delete(self, uid):
        return self.user_dao.delete(uid)

    def generate_password(self, password):
        hash_digest = hashlib.pdkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Конвертируем пароль в байты
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)