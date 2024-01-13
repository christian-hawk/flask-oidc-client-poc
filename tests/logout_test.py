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
  stored_original_method = session_handler.is_authenticated_session
  session_handler.is_authenticated_session = MagicMock()
  sut = logout.logout
  sut()
  session_handler.is_authenticated_session.assert_called_once()
  session_handler.is_authenticated_session = stored_original_method


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



sut2 = session_handler.clear_auth_session

def test_clear_auth_session_is_callable():
   assert (callable(sut2))

def test_clear_auth_session_calls_session_pop(client):
   with client.session_transaction() as session:
      session.pop = MagicMock()
      session['user'] = 'any user info'
      session['id_token'] = 'valid id token'
      sut2(session)
      session.pop.assert_any_call('user')
      session.pop.assert_any_call('id_token')
      assert session.pop.call_count == 2

def test_clear_auth_session_calls_returns_clear_session(client):
   with client.session_transaction() as session:
      session['user'] = 'any user info'
      session['id_token'] = 'valid id token'
      response = sut2(session)
      assert ('user' not in response)
      assert ('id_token' not in response)
