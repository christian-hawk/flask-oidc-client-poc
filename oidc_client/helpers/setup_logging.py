
import logging

def setup_logging(
    file: str = 'poc.log', 
    format: str = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s', 
    datefmt: str = '%m/%d/%Y %I:%M:%S %p',
    level: int = logging.DEBUG) -> None:
  
    logging.basicConfig(
        filename=file,
        format=format, 
        datefmt=datefmt, 
        level=level)