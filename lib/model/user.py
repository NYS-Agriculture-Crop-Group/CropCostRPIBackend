from lib.model.database import PostgresqlDB

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

    @staticmethod
    def createUser(username: str, password: str):
        cursor = PostgresqlDB.get_new_cursor()
        query = "SELECT * FROM users WHERE users.username = '{}';".format(username)
        cursor.execute(query)
        if len(cursor.fetchall()) != 0:
            print("User already exists")
            return None
        else:
            password_encoded = password
            query = "INSERT INTO users VALUES(DEFAULT, '{}', '{}');".format(username, password_encoded)
            cursor.execute(query)
            new_obj = cursor.findall()
            print("New User Created",new_obj)
            return new_obj