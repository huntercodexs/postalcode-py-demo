import requests

from library.library_postalcode_validator import PostalCodeValidatorLibrary


def dispatch_by_requests_simple(code:str):

    postalcode_validator = PostalCodeValidatorLibrary()
    code = postalcode_validator.postalcode_validator(code)

    url_service = f'https://viacep.com.br/ws/{code}/json/'
    response = requests.get(url=url_service)
    return response.json()

