import os
import psycopg2
from psycopg2.extras import DictCursor

class PostgresqlDB(object):
    PostgresqIDBinstance = None

    @classmethod
    def get_instance(cls):
        return cls.PostgresqIDBinstance

    @classmethod
    def connect(cls):
        if cls.PostgresqIDBinstance is None:
            cls.PostgresqIDBinstance = WrappedPostgresqlDB()
        return cls.PostgresqIDBinstance.wrapped_connect()

    @classmethod
    def get_new_cursor(cls):
        if cls.PostgresqIDBinstance is None:
            cls.PostgresqIDBinstance = WrappedPostgresqlDB()
        return cls.PostgresqIDBinstance.wrapped_get_new_cursor()

class WrappedPostgresqlDB(object):
    connection = None
    cursor = None

    @classmethod
    def wrapped_connect(cls):
        print("I am connecting to the database")
        username = os.getenv("POSTGRESUSER")
        password = os.getenv("POSTGRESPASS")
        print(username, password)
        cls.connection = psycopg2.connect(user="POSTGRESUSER", password="POSTGRESPASS", database='cropcost')
        #cls.connection = psycopg2.connect(user=username, password=password, database='cropcost')
        
        return cls.connection.cursor()

    @classmethod
    def wrapped_get_new_cursor(cls):
        if cls.connection is None:
           cls.wrapped_connect()
        return cls.connection.cursor(cursor_factory=DictCursor)

    @classmethod
    def wrapped_get_connection(cls):
        if cls.connection is None:
            cls.wrapped_connect()
        return cls.connection.cursor(cursor_factory=DictCursor)
