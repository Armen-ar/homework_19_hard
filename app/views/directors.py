from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.director import DirectorSchema
from app.helpers.decorators import auth_required, admin_required
from app.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """Представление возвращает всех режиссёров, допуск auth"""
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """Представление добавляет нового режиссёра, допуск admin"""
        req_json = request.json
        new_director = director_service.create(req_json)

        return f"Режиссёр с id {new_director.id} создан!", 201


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    @auth_required
    def get(self, uid):
        """Представление возвращает данные режиссёра по id, допуск auth"""
        r = director_service.get_one(uid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, uid: int):
        """Представление обновляет данные режиссёра по id, допуск admin"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, uid: int):
        """Представление удаляет данные режиссёра по id, допуск admin"""
        director_service.delete(uid)
        return "", 204

    @admin_required
    def patch(self, uid):
        """Представление обновляет частично данные режиссёра по id, допуск admin"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        director_service.update_partical(req_json)
        return "", 204
