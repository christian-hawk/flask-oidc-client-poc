from oidc_client import logout, create_app
from oidc_client.helpers import session_handler
import pytest
from flask import Flask, testing
from unittest.mock import MagicMock

  # Check if session is active (Credential exists)
  # saves id_token as token_hint
  # delete id_token from session
  # delete user(info) from session
  # Redirects to end_session_endpoint with post_logout_redirect_uri and token_hint


def test_logout_exists():
  import oidc_client
  print(oidc_client)
  assert hasattr(oidc_client.logout, 'logout')



@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "LIVESERVER_PORT": 9090,
        # Other test configurations
    })
    yield app

@pytest.fixture()
def client(app: Flask) -> testing.FlaskClient :
    return app.test_client()

def test_logout_should_check_if_session_is_active():
  session_handler.is_authenticated_session = MagicMock()
  sut = logout.logout
  sut()
  session_handler.is_authenticated_session.assert_called_once()


sut = session_handler.is_authenticated_session

# class TestIfAuthenticatedSessionExists():
#   # checks if id_token and user in session keys



def test_is_auth_session_should_be_callable():
  assert (callable(sut))

def test_is_auth_session_should_return_false_if_no_session(client):
  with client.session_transaction() as session:
     assert sut(session) is False

def test_is_auth_session_should_return_false_if_authenticated_session(client):
  with client.session_transaction() as session:
     session['id_token'] = 'any valid id_token'
     assert sut(session) is True

