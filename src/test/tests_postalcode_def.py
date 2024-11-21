import unittest
from unittest.mock import patch

from function.function_postalcode_http_client import dispatch_by_http_client


class TestPostalCode(unittest.TestCase):

    @patch('postalcode_def.requester')
    def test_postalcode_ok(self, mock_requester):
        mock_requester.return_value = {
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

        result = dispatch_by_http_client(event, None)
        self.assertEqual(result['cep'], '12090-002')
        print('OK2')

if __name__ == '__main__':
    unittest.main()