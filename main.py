# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
import app as app
from flask import Flask
from flask_restx import Api

from app.config1 import Config
from app.dao.model.users import User
from app.setup_db import db
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns       # Импорт
from app.views.users import user_ns


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()

    return app

# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def configure_app(app: Flask):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)


if __name__ == '__main__':
    app = create_app(Config())
    configure_app(app)
    app.run()
