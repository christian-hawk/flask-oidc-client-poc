from flask.sessions import SessionMixin

def is_authenticated_session(session: SessionMixin) -> bool:
  if 'id_token' in session.keys():
    return True
  else:
    return False
  
def clear_auth_session(session: SessionMixin) -> SessionMixin:
  session.pop('user')
  session.pop('id_token')
  return session
  
def get_token_hint(session: SessionMixin) -> str:
  token_hint = session.get('id_token')
  return token_hint