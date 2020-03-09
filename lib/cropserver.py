from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, Blueprint
from flask_restful import Resource, Api
from lib.resources.depriciatingAssets import DepriciatingAssetResource
from lib.model.database import PostgresqlDB
from lib.resources.authenticate import RegistationResource


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = os.getenv("SECRET")
PostgresqlDB.connect()

api = Api(app)

api.add_resource(DepriciatingAssetResource, '/dp')
api.add_resource(RegistationResource, '/auth')