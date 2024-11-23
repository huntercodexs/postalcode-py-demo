from unittest import TestCase
from unittest.mock import MagicMock

from main_postalcode_class_http_client import PostalCodeHttpClientClazz, lambda_handler


class PostalCodeTest(TestCase):

    def setUp(self):
        self.mock_postalcode_handle_api_lib = MagicMock()
        self.mock_postalcode_handle_api_req = MagicMock()

        self.postalcode_query = PostalCodeHttpClientClazz(
            postalcode_lib=self.mock_postalcode_handle_api_lib,
            postalcode_req=self.mock_postalcode_handle_api_req
        )


    @staticmethod
    def default_value():
        return {
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
            'siafi': '7183'
        }


    def test_lambda_handler(self):
        event = {
            'postalcode': '12090002'
        }
        result = lambda_handler(event=event, context=None)
        self.assertEqual('12090-002', result['cep'])


    def test_lambda_handler_mock(self):
        self.mock_postalcode_handle_api_req.postalcode_requester.return_value = self.default_value()
        mock = {
            'postalcode_lib': self.mock_postalcode_handle_api_lib,
            'postalcode_req': self.mock_postalcode_handle_api_req
        }
        event = {
            'postalcode': '12090002'
        }
        result = lambda_handler(event=event, context=None, mock=mock)
        self.assertEqual('12090-002', result['cep'])


    def test_postalcode_http_client_clazz(self):

        self.mock_postalcode_handle_api_req.postalcode_requester.return_value = self.default_value()

        code = '12090-002'
        result = self.postalcode_query.dispatch(code=code)
        self.assertEqual('12090-002', result['cep'])
        self.assertEqual('Rua São Caetano', result['logradouro'])
        self.assertEqual('Campos Elíseos', result['bairro'])
        self.assertEqual('Taubaté', result['localidade'])
        self.assertEqual('SP', result['uf'])
        self.assertEqual('São Paulo', result['estado'])
        self.assertEqual('Sudeste', result['regiao'])


