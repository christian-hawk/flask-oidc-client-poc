from .helpers import session_handler
from flask import session

def logout():
  session_handler.is_authenticated_session(session)  
  ...