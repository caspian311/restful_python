from flask_restful import Resource
from sqlalchemy import create_engine

class Employees(Resource):
    def __init__(self):
        self.__db_connect = create_engine('sqlite:///chinook.db')

    def get(self):
        conn = self.__db_connect.connect()
        query = conn.execute("select * from employees")
        return {'employees': [i[0] for i in query.cursor.fetchall()]}

