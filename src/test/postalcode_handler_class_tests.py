import unittest
from unittest.mock import patch

from postalcode_handler_class import lambda_handler


class TestPostalCode(unittest.TestCase):

    @patch('postalcode_handler_class.lambda_handler')
    def test_postalcode_ok(self, mock_lambda_handler):
        mock_lambda_handler.return_value = {
            'cep': '12090-002',
            'logradouro': 'Rua São Caetano',
            'complemento': '',
            'unidade': '',
            'bairro': 'Campos Elíseos',
            'localidade': 'Taubaté',
            'uf': 'SP',
            'estado': 'São Paulo',
            'regiao': 'Sudeste',
            'ibge': '3554102',
            'gia': '6889',
            'ddd': '12',
            'siafi': '7183'}

        event = {
            'postalcode': '12090002'
        }

        result = lambda_handler(event, None)
        self.assertEqual(result['cep'], '12090-002')
        print('OK4')

if __name__ == '__main__':
    unittest.main()
