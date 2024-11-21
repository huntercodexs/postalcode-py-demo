import http.client
import json

from library.library_postalcode_validator import PostalCodeValidatorLibrary


class PostalCodeHttpClientClazz:

    def __init__(self, postalcode_library: PostalCodeValidatorLibrary = None):
        self.__postalcode_library = postalcode_library

    def dispatch(self, code:str):
        code = self.__postalcode_library.postalcode_validator(code=code)
        conn = http.client.HTTPSConnection('viacep.com.br')
        headers = {'Content-type': 'application/json'}

        conn.request('GET', f'/ws/{code}/json/', 'null', headers)
        response = json.loads(conn.getresponse().read().decode())

        print('CHAMOUUUU')

        return response

    