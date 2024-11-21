import requests

from library.library_postalcode_validator import PostalCodeValidatorLibrary


def dispatch_by_requests(code:str):

    postalcode_validator = PostalCodeValidatorLibrary()
    code = postalcode_validator.postalcode_validator(code)

    encoded_body = None
    headers = {'Content-type': 'application/json'}
    url_service = f'https://viacep.com.br/ws/{code}/json/'

    response = requests.request(method='GET', url=url_service, headers=headers, data=encoded_body)

    return response.json()

