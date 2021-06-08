from models.employee import Employee


class EmployeeService:
    @staticmethod
    def fetch_all(session):
        return session.query(Employee).all()

    @staticmethod
    def fetch_by_uuid(session, uuid):
        return session.query(Employee).filter_by(uuid=uuid).first()
