from faker import Faker

from views import db
from models.department import Department
from models.employee import Employee

def populate(departments= 10, employees_per_department=10):
    generator = Faker()
    employees = []
    for i in range(departments):
        for j in range(employees_per_department):
            employees.append(Employee(
                generator.name(), 
                generator.date_of_birth(),
                generator.random_int()
            ))
        db.session.add(Department(
            generator.company(), 
            employees[-employees_per_department:]
        ))
    
    for employee in employees:
        db.session.add(employee)
    
    db.session.commit()
    db.session.close()

if __name__ == '__main__':
    print('Populating db...')
    populate()
    print('DB populated successfully')
