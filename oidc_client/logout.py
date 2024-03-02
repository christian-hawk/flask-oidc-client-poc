from .helpers import session_handler
from flask import session, redirect, Blueprint, url_for, current_app
from oidc_client.config import END_SESSION_ENDPOINT, POST_LOGOUT_REDIRECT
from urllib.parse import urlencode
import logging

logger = logging.getLogger(__name__)

bp = Blueprint('logout', __name__)

@bp.route('/logout')

def logout():
  logger.info('called logout')
  if session_handler.is_authenticated_session(session):
    token_hint = session_handler.get_token_hint(session)
    session_handler.clear_auth_session(session)

    query_params = {
      'post_logout_redirect_uri': POST_LOGOUT_REDIRECT,
      'token_hint': token_hint
    }

    encoded_qs = urlencode(query_params)
    full_url = '%s?%s' % (END_SESSION_ENDPOINT, encoded_qs)
    logger.info('Redirecting to %s' % full_url)
    return redirect(full_url)
  else:
    return redirect('/')
