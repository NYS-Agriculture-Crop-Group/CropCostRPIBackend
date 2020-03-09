import os
import psycopg2
from psycopg2.extras import DictCursor

class PostgresqlDB(object):
    connection = None
    cursor = None

    @classmethod
    def connect(cls):
        print("I am connecting to the database")
        username = os.getenv("POSTGRESUSER")
        password = os.getenv("POSTGRESPASS")
        print(username, password)
        cls.connection = psycopg2.connect(user=username, password=password, database='cropcost')

    @classmethod
    def get_new_cursor(cls):
        if cls.connection is None:
            cls.connect()
        else:
            return cls.connection.cursor(cursor_factory=DictCursor)