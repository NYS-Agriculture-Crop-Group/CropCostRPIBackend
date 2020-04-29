from lib.model.database import PostgresqlDB
import hashlib

class UserModel(object):

    @staticmethod
    def listusers():
        cursor = PostgresqlDB.get_new_cursor()
        query = "SELECT * FROM users;"
        cursor.execute(query)
        return cursor.fetchall()
    
    @staticmethod
    def getUserById(userid: str):
        cursor = PostgresqlDB.get_new_cursor()
        query = "SELECT * FROM users WHERE users.user_id = '{}';".format(userid)
        cursor.execute(query)
        return cursor.fetchone()

    @staticmethod
    def getUserByUsername(username: str):
        cursor = PostgresqlDB.get_new_cursor()
        query = "SELECT * FROM users WHERE users.username = '{}';".format(username)
        cursor.execute(query)
        return cursor.fetchone()
    
    def getUserByUsernameAndPass(username: str, password: str):
        password_encoded = hashlib.sha256(password.encode('utf-8')).hexdigest()
        cursor = PostgresqlDB.get_new_cursor()
        query = "SELECT * FROM users WHERE users.username = '{}' AND users.password='{}';".format(username, password_encoded)
        cursor.execute(query)
        return cursor.fetchone()

    @staticmethod
    def createUser(username: str, password: str):
        cursor = PostgresqlDB.get_new_cursor()
        query = "SELECT * FROM users WHERE users.username = '{}';".format(username)
        cursor.execute(query)
        exist_user = cursor.fetchone()
        if exist_user != None:
            print("User already exists")
            return exist_user.get('user_id')
        else:
            password_encoded = hashlib.sha256(password.encode('utf-8')).hexdigest()
            rowcount = cursor.rowcount
            query = "INSERT INTO users VALUES(DEFAULT, '{}', '{}');".format(username, password_encoded)
            cursor.execute(query)
            PostgresqlDB.get_connection().commit()
            if cursor.rowcount-rowcount != 1:
                print("Nothing was added")
                return cursor.lastrowid
            else:
                return cursor.lastrowid

    @staticmethod
    def verifyPassword(user_id: int, password: str):
        cursor = PostgresqlDB.get_new_cursor()
        query = "SELECT * FROM users WHERE users.user_id={};".format(user_id)
        cursor.execute(query)
        user = cursor.fetchone()
        if user is None:
            print("Cant verify pasword, user does not exist with id {}".format(user_id))
            return False
        else:
            password_hash = user.get('password')
            if password_hash == hashlib.sha256(password.encode('utf-8')):
                return True
            else:
                return False
