from datetime import datetime
import uuid
from views import db


class Employee(db.Model):
    '''
    Employee model


    Has 5 parameters: employee_name, date_of_birth, salary (required)
    and uuid (optional)
    '''
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    employee_name = db.Column(db.String(100), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, index=True, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    department = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __init__(self, employee_name: str, date_of_birth, salary: int):
        self.uuid = str(uuid.uuid4())
        self.employee_name = employee_name
        self.date_of_birth = date_of_birth
        self.salary = salary

    def __repr__(self) -> str:
        return f'Employee({self.uuid}, {self.employee_name},' + \
               f' {self.date_of_birth}, {self.salary})'
