
import logging
import sys

def setup_logging(
    format: str = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s', 
    datefmt: str = '%m/%d/%Y %I:%M:%S %p',
    level: int = logging.DEBUG,
    handlers: list = [ logging.StreamHandler(sys.stdout) ]) -> None:
  
    logging.basicConfig(
        format=format, 
        datefmt=datefmt, 
        level=level,
        handlers=handlers)