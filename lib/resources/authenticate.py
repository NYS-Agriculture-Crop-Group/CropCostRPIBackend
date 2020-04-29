"""
RegistrationResource represents a the rest endpoint used 
    for creating a new user
"""

from flask import request, g, Response
from flask_restful import Resource
import base64
from lib.model.user import UserModel
from lib.shared.authenticator import Authenticator
import json

class RegistationResource(Resource):

    def get(self):
        # get the requested username and password in format base64(username:password)
        auth_b64 = request.headers.get('Authorization')
        auth = base64.b64decode(auth_b64)
        auth = auth.decode()
        #auth = auth_b64
        # split the base 64 decoded string into username and password
        (username, password,) = auth.split(':')
        # check username and password
        if username is None:
            return {
                "status": "error",
                "message": "Auth header does not contain username"
            }
        
        if password is None:
            return {
                "status": "error",
                "message": "Auth Header does not contain password"
            }
        # create the requested user
        print("Got username {} pasword {}".format(username, password))
        #new_user_id = UserModel.createUser(username, password)
        
        user=UserModel.getUserByUsernameAndPass(username,password)
        # check that the new user was created
        if user is None:
            print("The User Exists")
            return {
                "status": "Error",
                "message": "A user with that name already exists"
            }
        else:
            g.user_id = user[0]
            new_user_id = str(user[0])
            # generate a JWT to allow the newly registered user to make resquests
            new_token = Authenticator.generate_token(new_user_id)
            # create response
            resp = Response()
            resp.data = json.dumps({"status": "success","userid":user[0]})
            resp.headers.add('JWT-Token', new_token)
            resp.headers.add('Content-Type', "text/json")
            return resp
