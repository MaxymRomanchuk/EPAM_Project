from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from rest.departmentSchema import DepartmentSchema
from views import db
from service.departmentService import DepartmentService


class DepartmentAPI(Resource):
    '''
    Department Resourse


    Supports GET (with UUID and without), POST, PUT and DELETE requests
    '''
    schema = DepartmentSchema()
    service = DepartmentService

    def get(self, uuid=None):
        if uuid:
            depts = [self.service.fetch_by_uuid(db.session, uuid)]
        else:
            depts = self.service.fetch_all(db.session)
        if not depts:
            return '', 404
        else:
            return self.schema.dump(depts, many=True), 200

    def post(self):
        try:
            dept = self.schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(dept)
        db.session.commit()
        return self.schema.dump(dept), 201

    def put(self, uuid):
        dept = self.service.fetch_by_uuid(db.session, uuid)
        if(not dept):
            return {'message': "wrong data..."}, 400

        try:
            dept = self.schema.load(request.json, instance=dept,
                                    session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400

        db.session.add(dept)
        db.session.commit()
        return self.schema.dump(dept), 200

    def delete(self, uuid):
        if not uuid:
            return {'message': "Bad request..."}, 401

        dept = self.service.fetch_by_uuid(db.session, uuid)
        if not dept:
            return '', 401

        db.session.delete(dept)
        db.session.commit()
        return '', 204
