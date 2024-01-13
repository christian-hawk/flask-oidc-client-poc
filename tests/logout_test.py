from oidc_client import logout
from oidc_client.helpers import is_authenticated_session
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

class TestIfAuthenticatedSessionExists():
  # checks if id_token and user in session keys

  sut = is_authenticated_session.is_authenticated_session

  def test_is_auth_session_should_be_callable(self):
    assert (callable(self.sut))