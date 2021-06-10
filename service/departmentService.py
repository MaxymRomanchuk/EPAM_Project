from models.department import Department


class DepartmentService:
    '''
    Static class for Department table query logic
    '''
    @staticmethod
    def fetch_all(session):
        return session.query(Department).all()

    @staticmethod
    def fetch_by_uuid(session, uuid):
        return session.query(Department).filter_by(uuid=uuid).first()
