import http.client
import json


class PostalCodeHandleApiLibrary:

    @staticmethod
    def postalcode_requester(code:str):
        print(f' >>> HANDLE-API -> Postalcode Requester for {code}')

        conn = http.client.HTTPSConnection('viacep.com.br')
        headers = {'Content-type': 'application/json'}

        conn.request('GET', f'/ws/{code}/json/', 'null', headers)
        response = json.loads(conn.getresponse().read().decode())

        return response
