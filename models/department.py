import uuid
from views import db


class Department(db.Model):
    '''
    Department object model


    Has 3 parameters: name (required), uuid and employees (optional)
    '''
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    employees = db.relationship('Employee', backref='department_id',
                                lazy='subquery')

    def __init__(self, name: str, employees=None):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.employees = employees if employees else []

    def __repr__(self) -> str:
        return f'Department({self.uuid}, {self.name})'
