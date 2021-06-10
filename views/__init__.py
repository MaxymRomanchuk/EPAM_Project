from flask import Flask, request, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import config

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static'
            )
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
cors = CORS(app=app)


@app.route('/')
def index():
    '''
    Returns page with main urls
    '''
    depts = str(request.base_url + 'departments')
    employees = str(request.base_url + 'employees')
    api_url = str(request.base_url + 'api')
    aligner = 'style="width: 400px; margin:0 auto;"'
    return f'<h3 {aligner}>Departments: <a href={depts}>{depts}</a></h3>' + \
        f'<h3 {aligner}>Employees: <a href={employees}>{employees}</a></h3>' +\
        f'<h3 {aligner}>Swagger: <a href={api_url}>{api_url}</a></h3>'


@app.route('/api')
def swagger():
    '''
    Renders swagger UI
    '''
    return render_template('swaggerui.html')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


from . import routes
