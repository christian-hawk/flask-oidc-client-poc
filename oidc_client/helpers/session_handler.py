from flask.sessions import SessionMixin
import logging

logger = logging.getLogger(__name__)

def is_authenticated_session(session: SessionMixin) -> bool:
  logger.info('is_authenticated_session called')
  if 'id_token' in session.keys():
    logger.debug('session is authenticated')
    return True
  else:
    logger.debug('session is not authenticated')
    return False
  
def clear_auth_session(session: SessionMixin) -> SessionMixin:
  logger.info('clear_auth_session called')
  session.pop('user')
  session.pop('id_token')
  return session
  
def get_token_hint(session: SessionMixin) -> str:
  logger.info('get_token_hint called')
  token_hint = session.get('id_token')
  return token_hint