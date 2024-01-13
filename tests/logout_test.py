from oidc_client import logout, create_app
from oidc_client.helpers import is_authenticated_session
import pytest
from flask import Flask, testing

# class TestLogout:

#   # Check if session is active (Credential exists)
#   # saves id_token as token_hint
#   # delete id_token from session
#   # delete user(info) from session
#   # Redirects to end_session_endpoint with post_logout_redirect_uri and token_hint


#   def test_logout_exists(self):
#     import oidc_client
#     print(oidc_client)
#     assert hasattr(oidc_client, 'logout')

#   def test_logout_should_check_if_session_is_active(self):
#     ...


sut = is_authenticated_session.is_authenticated_session


# class TestIfAuthenticatedSessionExists():
#   # checks if id_token and user in session keys

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




def test_is_auth_session_should_be_callable():
  assert (callable(sut))

def test_is_auth_session_should_return_false_if_no_session(client):
  with client.session_transaction() as session:
     assert sut(session) is False
