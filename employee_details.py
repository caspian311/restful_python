from flask_restful import Resource
from sqlalchemy import create_engine

class EmployeeDetails(Resource):
    def __init__(self):
        self.__db_connect = create_engine('sqlite:///chinook.db')

    def get(self, employee_id):
        conn = self.__db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

