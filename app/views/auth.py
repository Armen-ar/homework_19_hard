from flask import request
from flask_restx import Namespace, Resource

from app.implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthsView(Resource):
    def post(self):
        reg_json = request.json

        username = reg_json.get("username", None)
        password = reg_json.get("password", None)

        if None in [username, password]:
            return "", 401

        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201

    def put(self):
        reg_json = request.json
        token = reg_json.get("refresh_token")

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
