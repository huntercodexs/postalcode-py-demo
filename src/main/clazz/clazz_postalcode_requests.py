import requests

from library.library_postalcode_validator import PostalCodeValidatorLibrary


class PostalCodeRequestsClazz:

    def __init__(self, postalcode_library: PostalCodeValidatorLibrary = None):
        self.__postalcode_library = postalcode_library

    def dispatch(self, code:str):
        code = self.__postalcode_library.postalcode_validator(code=code)
        encoded_body = None
        headers = {'Content-type': 'application/json'}
        url_service = f'https://viacep.com.br/ws/{code}/json/'

        response = requests.request(method='GET', url=url_service, headers=headers, data=encoded_body)

        return response.json()

    