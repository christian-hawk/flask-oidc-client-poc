from oidc_client import logout, create_app, config
from oidc_client.helpers import session_handler
import pytest
from flask import Flask, testing, url_for, redirect
from unittest.mock import MagicMock, Mock
from oidc_client.logout import session as client_session
from urllib.parse import urlencode


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

def test_logout_should_check_if_session_is_active(client):
  original_is_authenticated_session = session_handler.is_authenticated_session
  original_clear_auth_session = session_handler.clear_auth_session
  original_get_token_hint = session_handler.get_token_hint
  with client.session_transaction() as session:
    session_handler.is_authenticated_session = MagicMock(return_value = True)
    session_handler.clear_auth_session = Mock(return_value = session)
    session_handler.get_token_hint = MagicMock(return_value = 'whatever token hint')
    sut = logout.logout
    sut()
    session_handler.is_authenticated_session.assert_called_once()
  
  session_handler.is_authenticated_session = original_is_authenticated_session
  session_handler.clear_auth_session = original_clear_auth_session
  session_handler.get_token_hint = original_get_token_hint

def test_logout_should_clear_auth_session_if_session_is_active(client):
  original_is_authenticated_session = session_handler.is_authenticated_session
  original_clear_auth_session = session_handler.clear_auth_session
  original_get_token_hint = session_handler.get_token_hint

  with client.session_transaction() as session:
      session_handler.is_authenticated_session = MagicMock(return_value = True)
      session_handler.clear_auth_session = Mock()
      session_handler.get_token_hint = MagicMock()
      session['id_token'] = 'any valid id_token'
      session['user'] = 'any valid user object'
      sut = logout.logout
      sut()
      session_handler.clear_auth_session.assert_called_once()

  session_handler.is_authenticated_session = original_is_authenticated_session
  session_handler.clear_auth_session = original_clear_auth_session
  session_handler.get_token_hint = original_get_token_hint

def test_logout_should_NOT_clear_auth_session_if_session_is_inactive(client):
  original_is_authenticated_session = session_handler.is_authenticated_session
  original_clear_auth_session = session_handler.clear_auth_session
  original_get_token_hint = session_handler.get_token_hint  

  session_handler.is_authenticated_session = MagicMock(return_value = False)
  session_handler.clear_auth_session = Mock(return_value = '')
  session_handler.get_token_hint = MagicMock(return_value = 'a')
  with client.session_transaction() as session:
      session['id_token'] = 'any valid id_token'
      session['user'] = 'any valid user object'
      sut = logout.logout
      response = sut()
      session_handler.clear_auth_session.assert_not_called()
  
  session_handler.is_authenticated_session = original_is_authenticated_session
  session_handler.clear_auth_session = original_clear_auth_session
  session_handler.get_token_hint = original_get_token_hint

def test_logout_should_get_token_hint(client):
  original_is_authenticated_session = session_handler.is_authenticated_session
  original_clear_auth_session = session_handler.clear_auth_session
  original_get_token_hint = session_handler.get_token_hint

  with client.session_transaction() as session:
      local_sut = logout.logout
      session_handler.is_authenticated_session = MagicMock(return_value = True)
      session_handler.clear_auth_session = Mock()
      session_handler.get_token_hint = MagicMock()
      local_sut()
      session_handler.get_token_hint.assert_called_once()
  
  session_handler.is_authenticated_session = original_is_authenticated_session
  session_handler.clear_auth_session = original_clear_auth_session
  session_handler.get_token_hint = original_get_token_hint


def test_logout_should_NOT_get_token_hint(client):
  original_is_authenticated_session = session_handler.is_authenticated_session
  original_clear_auth_session = session_handler.clear_auth_session
  original_get_token_hint = session_handler.get_token_hint

  with client.session_transaction() as session:
     # no id_token
      session_handler.is_authenticated_session = MagicMock(return_value = False)
      session_handler.clear_auth_session = Mock()
      session_handler.get_token_hint = MagicMock()

      local_sut = logout.logout
      local_sut()

      session_handler.get_token_hint.assert_not_called()

  session_handler.is_authenticated_session = original_is_authenticated_session
  session_handler.clear_auth_session = original_clear_auth_session
  session_handler.get_token_hint = original_get_token_hint


def test_logout_calls_redirect(client):
  original_is_authenticated_session = session_handler.is_authenticated_session
  original_clear_auth_session = session_handler.clear_auth_session
  original_get_token_hint = session_handler.get_token_hint

  session_handler.is_authenticated_session = MagicMock(return_value = True)
  session_handler.clear_auth_session = Mock()
  session_handler.get_token_hint = MagicMock(return_value = 'valid token hint')

  with client:
    query_params = {
      'post_logout_redirect_uri': config.POST_LOGOUT_REDIRECT,
      'token_hint': 'valid token hint'
    }
    encoded_qs = urlencode(query_params)
    expected_location = '%s?%s' % (config.END_SESSION_ENDPOINT, encoded_qs)
    local_sut = logout.logout
    assert local_sut().status_code == 302
    assert local_sut().location == expected_location
    
  
  session_handler.is_authenticated_session = original_is_authenticated_session
  session_handler.clear_auth_session = original_clear_auth_session
  session_handler.get_token_hint = original_get_token_hint


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

# session handler get token_hint
def test_get_token_hint_is_callabe():
   local_sut = session_handler.get_token_hint
   assert callable(local_sut)

def test_get_token_hint_should_call_session_get(client):
  local_sut = session_handler.get_token_hint
  with client.session_transaction() as session:
    session.get = MagicMock()
    local_sut(session)
    session.get.assert_called_once_with('id_token')

def test_get_token_hint_should_return_id_token(client):
   
   local_sut = session_handler.get_token_hint
   with client.session_transaction() as session:
     session['id_token'] = 'any valid id token'
     print(session.get('id_token'))
     expected = 'any valid id token'
     assert local_sut(session) == expected

