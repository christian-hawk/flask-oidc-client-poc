import unittest.mock as mock
from oidc_client.helpers.setup_logging import setup_logging
from oidc_client.helpers import setup_logging as setup_logging_file
import logging
import sys

@mock.patch('logging.basicConfig')
def test_setup_logging_called_with_params(mock_basicConfig):
  # Call the function with sample arguments
  setup_logging(handlers='test.log',
                format='[%(asctime)s] %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y',
                level=logging.INFO)

  # Check that basicConfig was called with the correct arguments
  mock_basicConfig.assert_called_once_with(handlers='test.log',
                                            format='[%(asctime)s] %(levelname)s: %(message)s',
                                            datefmt='%m/%d/%Y',
                                            level=logging.INFO)
  

@mock.patch('logging.basicConfig')
def test_setup_logging_defaults_no_args(mock_basicConfig):
  # TODO: Test handler mocking Streamhandler

  default_format = setup_logging_file.DEFAULT_FORMAT
  default_datefmt = setup_logging_file.DEFAULT_DATEFMT
  default_level = setup_logging_file.DEFAULT_LEVEL
  default_handlers = setup_logging_file.DEFAULT_HANDLERS
  
  setup_logging_file.setup_logging()

  mock_basicConfig.assert_called_once_with(format=default_format,
                                          datefmt=default_datefmt,
                                          level=default_level,
                                          handlers = default_handlers
                                          )

