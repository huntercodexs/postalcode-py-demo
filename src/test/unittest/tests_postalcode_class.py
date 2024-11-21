import unittest

from clazz.clazz_postalcode_http_client import PostalCodeHttpClientClazz


class TestPostalCode():

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

        result = PostalCodeHttpClientClazz.dispatch(event, None)
        self.assertEqual(result['cep'], '12090-002')
        print('OK1')

if __name__ == '__main__':
    unittest.main()
