import pytest
from flask import url_for, session
from unittest.mock import patch, MagicMock
from oidc_client import oauth, create_app  # import oauth client and the app from your application module

app = create_app()
@pytest.fixture
def client():
    with app.app_context():
        app.config["TESTING"] = True
        app.config['SERVER_NAME'] = 'localhost.localdomain'
        with app.test_client() as client:
            yield client

@patch.object(oauth, 'op')
def test_callback_missing_code(mocked_op, client):
    with app.app_context():
        res = client.get(url_for('callback'))
    assert res.status_code == 400
    assert session.get('id_token') is None
    assert session.get('user') is None

@patch.object(oauth, 'op')
def test_callback_valid_code(mocked_op, client):
    mocked_op.authorize_access_token.return_value = {'id_token': 'example_token'}
    mocked_op.userinfo.return_value = {'user_info': 'example_user_info'}
    with app.app_context():
        res = client.get(url_for('callback'), query_string={'code': 'valid_code'})
    assert res.status_code == 302
    assert session.get('id_token') == 'example_token'
    assert session.get('user') == {'user_info': 'example_user_info'}

@patch.object(oauth, 'op')
def test_callback_invalid_code(mocked_op, client):
    mocked_op.authorize_access_token.side_effect = Exception("Error")  # simulate exception
    with app.app_context():
        res = client.get(url_for('callback'), query_string={'code': 'invalid_code'})
    assert res.status_code == 500
    assert session.get('id_token') is None
    assert session.get('user') is None

@patch.object(oauth, 'op')
def test_callback_userinfo_exception(mocked_op, client):
    mocked_op.authorize_access_token.return_value