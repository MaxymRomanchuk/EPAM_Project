from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from rest.employeeSchema import EmployeeSchema
from views import db
from service.employeeService import EmployeeService


class EmployeeAPI(Resource):
    '''
    Employee Resourse


    Supports GET (with UUID and without), POST, PUT and DELETE requests
    '''
    schema = EmployeeSchema()
    service = EmployeeService

    def get(self, uuid=None):
        if uuid:
            employees = [self.service.fetch_by_uuid(db.session, uuid)]
        else:
            employees = self.service.fetch_all(db.session)
        if not employees:
            return '', 404
        else:
            return self.schema.dump(employees, many=True), 200

    def post(self):
        try:
            employee = self.schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(employee)
        db.session.commit()
        return self.schema.dump(employee), 201

    def put(self, uuid):
        employee = self.service.fetch_by_uuid(db.session, uuid)
        if(not employee):
            return {'message': "Employee uuid not found..."}, 404
        else:
            try:
                employee = self.schema.load(request.json, instance=employee,
                                            session=db.session)
            except ValidationError as e:
                return {'message': str(e)}, 400
        db.session.add(employee)
        db.session.commit()
        return self.schema.dump(employee), 200

    def delete(self, uuid):
        if not uuid:
            return {'message': "Bad request..."}, 401
        employee = self.service.fetch_by_uuid(db.session, uuid)
        if not employee:
            return '', 401
        db.session.delete(employee)
        db.session.commit()
        return '', 204
