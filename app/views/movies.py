from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.movie import MovieSchema
from app.helpers.decorators import auth_required, admin_required
from app.implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """Представление возвращает все фильмы или фильмы по режиссёрам, жанрам и годам, допуск auth"""
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200

    @admin_required
    def post(self):
        """Представление добавляет новый фильм, допуск admin"""
        req_json = request.json
        movie = movie_service.create(req_json)
        return f"Фильм с id {movie.id} создан!", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        """Представление возвращает фильм по id, допуск auth"""
        b = movie_service.get_one(mid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    @admin_required
    def put(self, mid):
        """Представление обновляет фильм по id, допуск admin"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = mid
        movie_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, mid):
        """Представление удаляет фильм по id, допуск admin"""
        movie_service.delete(mid)
        return "", 204

    @admin_required
    def patch(self, mid):
        """Представление обновляет частично фильм по id, допуск admin"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = mid
        movie_service.update_partical(req_json)
        return "", 204
