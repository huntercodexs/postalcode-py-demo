import http.client
import json


def lambda_handler(event, context):
    return PostalCode.requester(event['postalcode'])


class PostalCode:
    @staticmethod
    def requester(code):
        conn = http.client.HTTPSConnection('viacep.com.br')
        headers = {'Content-type': 'application/json'}

        conn.request('GET', '/ws/' + code + '/json/', 'null', headers)
        response = json.loads(conn.getresponse().read().decode())

        return response

