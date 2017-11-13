from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from employees import Employees
from tracks import Tracks
from employee_details import EmployeeDetails

app = Flask(__name__)
api = Api(app)

api.add_resource(Employees, '/employees')
api.add_resource(Tracks, '/tracks') 
api.add_resource(EmployeeDetails, '/employees/<employee_id>') 

if __name__ == '__main__':
     app.run(port='5002')
     
