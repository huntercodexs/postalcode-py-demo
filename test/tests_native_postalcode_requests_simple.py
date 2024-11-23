from time import sleep

from main_postalcode_def_requests_simple import lambda_handler


def test_lambda_handler_successfully():

    event = {
        'postalcode': '12090002'
    }

    result = lambda_handler(event, None)
    assert result['cep'] == '12090-002'

def test_lambda_handler_error():

    event = {
        'postalcode': '82009020'
    }

    result = lambda_handler(event, None)
    assert result['erro'] == 'true'

def test_lambda_handler_invalid_code():

    event = {
        'postalcode': '120090204'
    }

    try:
        lambda_handler(event, None)
    except ValueError as e:
        assert 1 == 1

# NOTE:
# To run these tests don't install the frameworks for tests purpose, for example: pytest, mock, unittest, etc.
# In case there is anyone of these frameworks installed in your .env python do the following instruction:
#
# pip uninstall pytest
# pip uninstall mock
# pip uninstall magicmock
#
if __name__ == "__main__":
    test_lambda_handler_successfully()
    print('test_lambda_handler_successfully - PASSED')
    sleep(1)
    test_lambda_handler_error()
    print('test_lambda_handler_error - PASSED')
    sleep(1)
    test_lambda_handler_invalid_code()
    print('test_lambda_handler_invalid_code - PASSED')

