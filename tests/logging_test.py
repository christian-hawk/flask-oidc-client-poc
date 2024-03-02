import unittest.mock as mock
from oidc_client.helpers.setup_logging import setup_logging
import logging

@mock.patch('logging.basicConfig')
def test_setup_logging_called_with_params(mock_basicConfig):
  # Call the function with sample arguments
  setup_logging(file='test.log',
                format='[%(asctime)s] %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y',
                level=logging.INFO)

  # Check that basicConfig was called with the correct arguments
  mock_basicConfig.assert_called_once_with(filename='test.log',
                                            format='[%(asctime)s] %(levelname)s: %(message)s',
                                            datefmt='%m/%d/%Y',
                                            level=logging.INFO)
  
@mock.patch('logging.basicConfig')
def test_setup_logging_defaults_no_args(mock_basicConfig):

  default_file : str = 'poc.log'
  default_format : str =  '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
  default_datefmt : str = '%m/%d/%Y %I:%M:%S %p'
  default_level :  int = logging.DEBUG
  
  # Call function with no arguments
  setup_logging()

  mock_basicConfig.assert_called_once_with(filename=default_file,
                                           format=default_format,
                                           datefmt=default_datefmt,
                                           level=default_level)

