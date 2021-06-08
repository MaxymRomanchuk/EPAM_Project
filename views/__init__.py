from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)


@app.route('/')
def index():
    depts = str(request.base_url + 'departments')
    employees = str(request.base_url + 'employees')
    aligner = 'style="width: 400px; margin:0 auto;"'
    return f'<h3 {aligner}>Departments: <a href={depts}>{depts}</a></h3>' + \
        f'<h3 {aligner}>Employees: <a href={employees}>{employees}</a></h3>'


from vievs import routes
