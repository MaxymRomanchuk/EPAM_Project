from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.employee import Employee


class EmployeeSchema(SQLAlchemyAutoSchema):
    '''
    AutoSchema for EmployeeAPI request validation
    '''
    class Meta:
        model = Employee
        exclude = ['id']
        load_instance = True
