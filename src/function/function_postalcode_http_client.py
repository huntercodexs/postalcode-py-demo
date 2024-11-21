import http.client
import json

from library.library_postalcode_validator import PostalCodeValidatorLibrary


def dispatch_by_http_client(code:str):

    postalcode_validator = PostalCodeValidatorLibrary()
    code = postalcode_validator.postalcode_validator(code)

    conn = http.client.HTTPSConnection('viacep.com.br')
    headers = {'Content-type': 'application/json'}

    conn.request('GET', f'/ws/{code}/json/', 'null', headers)
    response = json.loads(conn.getresponse().read().decode())

    return response

