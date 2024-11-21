import requests

from library.library_postalcode_validator import PostalCodeValidatorLibrary


class PostalCodeRequestsSimpleClazz:

    def __init__(self, postalcode_library: PostalCodeValidatorLibrary = None):
        self.__postalcode_library = postalcode_library

    def dispatch(self, code:str):
        code = self.__postalcode_library.postalcode_validator(code=code)
        url_service = f'https://viacep.com.br/ws/{code}/json/'
        response = requests.get(url=url_service)
        return response.json()

    