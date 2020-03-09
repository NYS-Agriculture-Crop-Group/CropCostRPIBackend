import sqlalchemy.orm.session as ses
from flask_restful import Resource
from flask import request, jsonify, g
from lib.model.database import PostgresqlDB
from lib.model.user import UserModel
from lib.shared.authenticator import Authenticator
class UserResource(Resource):
    
    @Authenticator.auth_required
    def get(self):
        user_id = g.id
        user = UserModel.getUserById(user_id)
        return user

    def post(self):
        return {"Message": "DepricitingAssetPost"}