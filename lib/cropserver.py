from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask, Blueprint
from flask_restful import Resource, Api
from lib.resources.depriciatingAssets import DepriciatingAssetResource
from lib.model.database import PostgresqlDB
from lib.resources.authenticate import RegistationResource
from lib.resources.users import UserResource
from flask import request, g, Response,render_template


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = os.getenv("SECRET")
PostgresqlDB.connect()

@app.route('/login/')
def login(name=None):
    return render_template('login.html', name=name)
  
api = Api(app)

api.add_resource(DepriciatingAssetResource, '/dp')
api.add_resource(RegistationResource, '/auth')
api.add_resource(UserResource,'/machines')
