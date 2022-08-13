import jwt
from flask import request, abort

from app.helpers.constants import SECRET, ALGORITHM


def auth_required(func):
    """
    Метод проверяет авторизацию, наличие токена и его декодирование
    """
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        print(token)
        try:
            jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """
    Метод проверяет авторизацию, наличие токена, его декодирование и допуск к информации
    """
    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        role = None

        try:
            user = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
            role = user.get("role", "user")
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        if role != "admin":
            abort(403)

        return func(*args, **kwargs)

    return wrapper
