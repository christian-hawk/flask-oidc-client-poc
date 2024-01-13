from flask.sessions import SessionMixin

def is_authenticated_session(session: SessionMixin) -> bool:
  if 'id_token' in session.keys():
    return True
  else:
    return False
  