from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.department import Department


class DepartmentSchema(SQLAlchemyAutoSchema):
    '''
    AutoSchema for DepartmentAPI request validation
    '''
    class Meta:
        model = Department
        exclude = ['id']
        load_instance = True
