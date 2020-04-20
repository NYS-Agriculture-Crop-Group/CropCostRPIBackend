import os
import psycopg2
from psycopg2.extras import DictCursor

class PostgresqlDB(object):
    PostgresqIDBinstance = None

    def get_instance(self):
        return self.PostgresqIDBinstance

    def connect(cls):
        if PostgresqIDBinstance is None:
            PostgresqIDBinstance = WrappedPostgresqlDB()
        PostgresqIDBinstance.wrapped_connect(cls)

    def get_new_cursor(cls):
        if PostgresqlDBinstance is None:
            PostgresqIDBinstance = WrappedPostgresqlDB()
        return PostgresqIDBinstance.wrapped_get_new_cursor(cls)

    def get_new_cursor(cls):
        if PostgresqlDBinstance is None:
            PostgresqIDBinstance = WrappedPostgresqlDB()
        return PostgresqIDBinstance.wrapped_get_new_cursor(cls)

class WrappedPostgresqlDB(object):
    connection = None
    cursor = None

    @classmethod
    def wrapped_connect(cls):
        print("I am connecting to the database")
        username = os.getenv("POSTGRESUSER")
        password = os.getenv("POSTGRESPASS")
        print(username, password)
        cls.connection = psycopg2.connect(user=username, password=password, database='cropcost')

    @classmethod
    def wrapped_get_new_cursor(cls):
        if cls.connection is None:
            cls.connect()
        else:
            return cls.connection.cursor(cursor_factory=DictCursor)

    @classmethod
    def wrapped_get_connection(cls):
        if cls.connection is None:
            cls.connect()
        else:
            return cls.connection
