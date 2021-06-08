from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.department import Department


class DepartmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        exclude = ['id']
        load_instance = True
