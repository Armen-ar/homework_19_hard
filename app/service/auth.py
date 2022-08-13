import calendar
import datetime

import jwt
from flask_restx import abort

from app.helpers.constants import SECRET, ALGORITHM
from app.service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        """
        Метод, который генерирует access_token и refresh_token, получая имя и пароль пользователя
        с проверкой is_refresh (создание новых токенов, а не перегенерация refresh_token)
        """
        user = self.user_service.get_by_username(username)

        if user is None:
            raise abort(404)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }
        # 30 min for access_token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)

        # 130 days for refresh_token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        """
        Метод получает информацию о пользователе, извлекает значение 'username' и по refresh_token,
        который получил в методе generate_tokens вызывает этот же метод и передаёт туда только
        username и получает новую пару токенов
        """
        data = jwt.decode(jwt=refresh_token, key=SECRET, algorithms=[ALGORITHM])
        username = data.get("username")

        return self.generate_tokens(username, None, is_refresh=True)
