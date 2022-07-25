from app.dao.model.users import User, UserSchema
from app.setup_db import db     # Импорт


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        return self.session.query(User).all()

    def get_one(self, uid):
        return self.session.query(User).get_or_404(uid)

    # def get_by_username(self, username):
    #     return self.session(User).filter(User.username == username).first()

    def create(self, data):
        new_user = User(**data)

        db.session.add(new_user)
        db.session.commit()

        return new_user


    def update(self, uid, data):
        user = self.get_one(uid)

        user.title = data.get('title')
        user.description = data.get('description')
        user.trailer = data.get('trailer')
        user.year = data.get('year')
        user.rating = data.get('rating')
        user.genre_id = data.get('genre_id')
        user.director_id = data.get('director_id')

        db.session.add(user)
        db.session.commit()


    def delete(self, uid):
        user = self.get_one(uid)

        db.session.delete(user)
        db.session.commit()