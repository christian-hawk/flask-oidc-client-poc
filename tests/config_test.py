from oidc_client import config

def test_if_metadata_url_exists():
  assert(hasattr(config, 'SERVER_META_URL'))

def test_if_client_id_exists():
  assert(hasattr(config, 'CLIENT_ID'))
  
def test_if_client_secret_exists():
  assert(hasattr(config, 'CLIENT_SECRET'))

def test_if_end_session_endpoint_exists():
  assert(hasattr(config, 'END_SESSION_ENDPOINT'))

def test_if_post_logout_redirect_exists():
  assert(hasattr(config, 'POST_LOGOUT_REDIRECT'))
