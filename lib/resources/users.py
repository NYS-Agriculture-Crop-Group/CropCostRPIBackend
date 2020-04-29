import sqlalchemy.orm.session as ses
from flask_restful import Resource
from flask import request, jsonify, g
from lib.model.database import PostgresqlDB
from lib.model.user import UserModel
from lib.shared.authenticator import Authenticator
class UserResource(Resource):
    
    @Authenticator.auth_required
    def get(self):
        user_id = request.args.get("userid")
        user = UserModel.getUserById(user_id)
        return user
    
    @Authenticator.auth_required
    def post(self):
        user_id = request.args.post("userid")
        user = UserModel.getUserById(user_id)
        return user
