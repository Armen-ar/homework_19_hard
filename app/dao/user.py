from app.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        """Метод возвращает пользователя по id"""
        return self.session.query(User).get(uid)

    def get_by_username(self, username):
        """Метод возвращает пользователя по имени"""
        return self.session.query(User).filter(User.username == username).one()

    def get_all(self):
        """Метод возвращает всех пользователей"""
        return self.session.query(User).all()

    def create(self, user_data):
        """Метод добавляет нового пользователя"""
        entity = User(**user_data)

        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, uid):
        """Метод удаляет пользователя по id"""
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()

    def update(self, user_data):
        """Метод обновляет данные пользователя по id"""
        uid = user_data.get("id")
        user = self.get_one(uid)

        user.username = user_data.get("username")
        user.password = user_data.get("password")
        user.role = user_data.get("role")

        self.session.add(user)
        self.session.commit()
