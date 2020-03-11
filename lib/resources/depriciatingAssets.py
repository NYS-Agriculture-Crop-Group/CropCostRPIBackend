"""
depriciatingAsset.py contains functinos relating to the depriciating
    asset table rest api endpoint
"""

import sqlalchemy.orm.session as ses
from flask_restful import Resource
from flask import g
from lib.model.database import PostgresqlDB
from lib.shared.authenticator import Authenticator

"""
DepriciatingAssetResource: the rest endpoint representing CRUD
    for the depriciating asset table
"""
class DepriciatingAssetResource(Resource):
    
    """
    get a list of all depriciating assets attached to a user id
    """
    @Authenticator.auth_required
    def get(self):
        user_id = g.id
        if user_id is None: # make sure a valid user id was specified
            return {
                "status": "error",
                "message": "no user id specified in the web token"
            }
        # run the query to get all depriciating assets tied to an account
        new_cursor = PostgresqlDB.get_new_cursor()
        new_cursor.execute("""
            SELECT *
            FROM dpassets
            WHERE dpassets.user_id={};
            """.format(user_id))
        return {
            "status": "success",
            "message": new_cursor.fetchall()
        }

    def post(self):
        return {"Message": "DepricitingAssetPost"}