from flask import request
from flask_restx import Namespace, Resource

from app.dao.model.user import UserSchema
from app.helpers.decorators import admin_required
from app.implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        """Представление возвращает всех пользователей"""
        users = user_service.get_all()
        response = UserSchema(many=True).dump(users)

        return response, 200

    def post(self):
        """Представление добавляет нового пользователя"""
        data = request.json
        user = user_service.create(data)

        return f"Пользователь с id {user.id} создан!", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @admin_required
    def delete(self, uid):
        """Представление удаляет пользователя по id, допуск auth"""
        user_service.delete(uid)

        return "", 204
