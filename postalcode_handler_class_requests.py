import requests


def lambda_handler(event, context):
    return PostalCode.requester(event)


class PostalCode:
    @staticmethod
    def requester(event):

        encoded_body = None
        headers = {'Content-type': 'application/json'}
        url_service = 'http://viacep.com.br/ws/' + event['postalcode'] + '/json/'

        response = requests.request(method='GET', url=url_service, headers=headers, data=encoded_body)

        response_body = None
        if response.content:
            response_body = response.json()

        return response_body

