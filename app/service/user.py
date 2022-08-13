import base64
import hashlib
import hmac

from app.helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from app.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        """Метод возвращает пользователя по id"""
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        """Метод возвращает пользователя по имени"""
        return self.dao.get_by_username(username)

    def get_all(self):
        """Метод возвращает всех пользователей"""
        return self.dao.get_all()

    def create(self, user_data):
        """Метод добавляет нового пользователя с хэшированным паролем"""
        user_data["password"] = self.generate_password(user_data["password"])
        return self.dao.create(user_data)

    def delete(self, uid):
        """Метод удаляет пользователя по id"""
        return self.dao.delete(uid)

    def update(self, user_data):
        """Метод обновления данных пользователя с хэшированным паролем"""
        user_data["password"] = self.generate_password(user_data["password"])
        self.dao.update(user_data)
        return self.dao

    def generate_password(self, password):
        """Метод хеширование пароля"""
        hash_password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_password)

    def compare_passwords(self, password_hash, other_password) -> bool:
        """Метод возвращает сравнение бинарных последовательностей чисел(из базы данных 'password_hash'
         и сгенерированный 'other_password'), возвращает либо True либо False
         """
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)
