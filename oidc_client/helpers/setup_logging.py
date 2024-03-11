import logging
import sys

DEFAULT_DATEFMT: str = '[%Y-%m-%d %H:%M:%S %z]'
DEFAULT_FORMAT: str = '%(asctime)s [%(process)s] [%(levelname)s] %(filename)s:%(funcName)s %(message)s'
DEFAULT_LEVEL: int = logging.INFO
DEFAULT_HANDLERS: list = [ logging.StreamHandler(sys.stderr) ]


def setup_logging(
    format: str = DEFAULT_FORMAT, 
    datefmt: str = DEFAULT_DATEFMT,
    level: int = DEFAULT_LEVEL,
    handlers: list = DEFAULT_HANDLERS
    ) -> None:
  
    logging.basicConfig(
        format=format, 
        datefmt=datefmt, 
        level=level,
        handlers=handlers
        )
