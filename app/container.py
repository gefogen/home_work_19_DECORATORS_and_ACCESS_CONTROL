# файл для создания DAO и сервисов чтобы импортировать их везде
from app.dao.directors import DirectorDAO
from app.dao.genres import GenreDAO
from app.dao.movies import MovieDAO
from app.dao.users import UserDAO
from app.service.auth import AuthService
from app.service.directors import DirectorService
from app.service.genres import GenreService
from app.service.movies import MovieService
from app.service.users import UserService
from app.setup_db import db  # Импорт

###### MOVIE ######
movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

###### DIRECTOR ######
director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

###### GENRE ######
genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

###### USER ######
user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

###### USER ######
auth_service = AuthService(user_service=user_service)
