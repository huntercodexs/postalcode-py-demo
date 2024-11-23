import unittest

from main_postalcode_class_http_client import lambda_handler


class PostalCodeTest(unittest.TestCase):

    def test_lambda_handler_successfully(self):

        event = {
            'postalcode': '12090002'
        }

        result = lambda_handler(event, None)
        self.assertEqual('12090-002', result['cep'])
        print('test_lambda_handler_successfully - PASSED')

    def test_lambda_handler_error(self):

        event = {
            'postalcode': '82009020'
        }

        result = lambda_handler(event, None)
        self.assertEqual('true', result['erro'])
        print('test_lambda_handler_error - PASSED')

    def test_lambda_handler_invalid_code(self):

        event = {
            'postalcode': '120090204'
        }

        try:
            lambda_handler(event, None)
        except ValueError as e:
            self.assertEqual(1, 1)
            print('test_lambda_handler_invalid_code - PASSED')


# NOTE:
# To run these tests you don't need to import any library or dependency, just use the unittest default
# library from python core
#
if __name__ == '__main__':
    unittest.main()

