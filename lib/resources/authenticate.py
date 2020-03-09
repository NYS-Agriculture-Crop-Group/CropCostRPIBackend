from flask import request, g, Response
from flask_restful import Resource
import base64
from lib.model.user import UserModel
from lib.shared.authenticator import Authenticator
import json

class RegistationResource(Resource):

    def get(self):
        auth_b64 = request.headers.get('Authorization')
        #auth = base64.b64decode(auth_b64)
        auth = auth_b64
        (username, password,) = auth.split(':')
        print("Got username {} pasword {}".format(username, password))
        new_user = UserModel.createUser(username, password)
        print("New user", new_user)
        if new_user is None:
            print("The User Exists")
            return {
                "status": "Error",
                "message": "A user with that name already exists"
            }
        else:
            user_obj = UserModel.createUser(username, password)
            new_token = Authenticator.generate_token(user_obj)
            resp = Response()
            resp.data = json.dumps({"status": "success"})
            resp.headers.add('JWT-Token', new_token)
            return {
                "status": "success"
            }
