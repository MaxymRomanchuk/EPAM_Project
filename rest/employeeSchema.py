from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.employee import Employee


class EmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        exclude = ['id']
        load_instance = True
