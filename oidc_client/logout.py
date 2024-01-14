from .helpers import session_handler
from flask import session


def logout():
  if session_handler.is_authenticated_session(session):
    session_handler.clear_auth_session(session)
