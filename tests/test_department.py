from unittest.mock import patch
from dataclasses import dataclass
from http import HTTPStatus
import json

from views import app


@dataclass
class FakeDepartment:
    name = 'Mr Wilson`s Bakery'
    employees = []


class TestDepartments:
    def test_get(self):
        client = app.test_client()
        resp = client.get('/departments')
        assert resp.status_code == HTTPStatus.OK

    def test_post_department(self):
        with patch('views.db.session.add', autospec=True
                   ) as mock_session_add, \
            patch('views.db.session.commit', autospec=True
                  ) as mock_session_commit:
            client = app.test_client()
            data = {
                    'name': 'Trainspotting'
                }
            response = client.post('/departments', data=json.dumps(data),
                                   content_type='application/json')

            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()

            assert response.status_code == HTTPStatus.CREATED
            assert response.json['name'] == data['name']

    def test_update_department(self):
        with patch(
            'service.departmentService.DepartmentService.fetch_by_uuid'
            ) as mock_fetch,\
            patch('views.db.session.add',
                  autospec=True) as mock_session_add, \
            patch('views.db.session.commit',
                  autospec=True) as mock_session_commit:
            client = app.test_client()
            mock_fetch.return_value = FakeDepartment()
            data = {
                    'name': 'Trainspotting'
                }
            response = client.put(
                '/department/1',
                data=json.dumps(data),
                content_type='application/json'
                )

            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()
            mock_fetch.assert_called_once()

            assert response.status_code == HTTPStatus.OK
            assert response.json['name'] == data['name']

    def test_delete_department(self):
        with patch(
            'service.departmentService.DepartmentService.fetch_by_uuid'
            ) as mock_fetch,\
            patch(
                'views.db.session.delete',
                autospec=True) as mock_session_delete, \
            patch(
                'views.db.session.commit',
                autospec=True) as mock_session_commit:

            client = app.test_client()
            mock_fetch.return_value = FakeDepartment()
            response = client.delete('/department/1')

            mock_session_delete.assert_called_once()
            mock_session_commit.assert_called_once()
            mock_fetch.assert_called_once()

            assert response.status_code == HTTPStatus.NO_CONTENT
