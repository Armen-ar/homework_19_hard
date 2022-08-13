from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema
from app.helpers.decorators import auth_required, admin_required
from app.implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        """Представление возвращает все жанры, допуск auth"""
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """Представление добавляет новый жанр, допуск admin"""
        req_json = request.json
        new_genre = genre_service.create(req_json)

        return f"Жанр с id {new_genre.id} создан!", 201


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    @auth_required
    def get(self, uid):
        """Представление возвращает жанр по id, допуск auth"""
        r = genre_service.get_one(uid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, uid: int):
        """Представление обновляет жанр по id, допуск admin"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        genre_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, uid: int):
        """Представление удаляет жанр по id, допуск admin"""
        genre_service.delete(uid)
        return "", 204

    @admin_required
    def patch(self, uid):
        """Представление обновляет частично жанр по id, допуск admin"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        genre_service.update_partical(req_json)
        return "", 204
