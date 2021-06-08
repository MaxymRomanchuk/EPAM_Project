from unittest.mock import patch
from dataclasses import dataclass
from http import HTTPStatus
import json

from views import app


@dataclass
class FakeEmployee:
    employee_name = 'Louis Armstrong'
    date_of_birth = "2011-11-11"
    salary = 500


class TestEmployees:
    def test_get(self):
        client = app.test_client()
        resp = client.get('/employees')
        assert resp.status_code == HTTPStatus.OK

    def test_post_employee(self):
        with patch('views.db.session.add', autospec=True) as mock_session_add,\
            patch('views.db.session.commit',
                  autospec=True) as mock_session_commit:
            client = app.test_client()
            data = {
                    'employee_name': 'Jack Son',
                    'date_of_birth': "2011-11-11",
                    'salary': 500
                }
            response = client.post(
                '/employees',
                data=json.dumps(data),
                content_type='application/json'
                )

            print(response.json)
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()

            assert response.status_code == HTTPStatus.CREATED
            assert response.json['employee_name'] == data['employee_name']

    def test_update_employee(self):
        with patch(
            'service.employeeService.EmployeeService.fetch_by_uuid'
            ) as mock_fetch,\
                patch('views.db.session.add',
                      autospec=True) as mock_session_add, \
                patch('views.db.session.commit',
                      autospec=True) as mock_session_commit:

            client = app.test_client()
            mock_fetch.return_value = FakeEmployee()
            data = {
                    'employee_name': 'Jack Son',
                    'date_of_birth': "2011-11-11",
                    'salary': 500
                }
            response = client.put(
                '/employee/1',
                data=json.dumps(data),
                content_type='application/json'
                )

            print(response.json)
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()
            mock_fetch.assert_called_once()

            assert response.status_code == HTTPStatus.OK
            assert response.json['employee_name'] == data['employee_name']

    def test_delete_employee(self):
        with patch(
            'service.employeeService.EmployeeService.fetch_by_uuid'
            ) as mock_fetch,\
                patch('views.db.session.delete',
                      autospec=True) as mock_session_delete, \
                patch('views.db.session.commit',
                      autospec=True) as mock_session_commit:

            client = app.test_client()
            mock_fetch.return_value = FakeEmployee()
            response = client.delete('/employee/1')

            mock_session_delete.assert_called_once()
            mock_session_commit.assert_called_once()
            mock_fetch.assert_called_once()

            assert response.status_code == HTTPStatus.NO_CONTENT
