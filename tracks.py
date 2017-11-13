from flask_restful import Resource
from sqlalchemy import create_engine

class Tracks(Resource):
    def __init__(self):
        self.__db_connect = create_engine('sqlite:///chinook.db')

    def get(self):
        conn = self.__db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
