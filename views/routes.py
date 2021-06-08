from rest.employeeApi import EmployeeAPI
from rest.departmentApi import DepartmentAPI
from views import api

api.add_resource(EmployeeAPI, '/employees', '/employee/<uuid>', 
    strict_slashes=False)
api.add_resource(DepartmentAPI, '/departments', '/department/<uuid>',
    strict_slashes=False)
