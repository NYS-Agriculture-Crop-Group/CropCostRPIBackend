import sqlalchemy.orm.session as ses
from flask_restful import Resource
from lib.model.database import PostgresqlDB

class DepriciatingAssetResource(Resource):
    
    def get(self):
        new_cursor = PostgresqlDB.get_new_cursor()
        new_cursor.execute("SELECT * FROM users;")
        return {"Message": new_cursor.fetchall()}

    def post(self):
        return {"Message": "DepricitingAssetPost"}