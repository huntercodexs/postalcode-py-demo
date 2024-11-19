import http.client
import json

def requester(event, context):
    code = event['postalcode']
    conn = http.client.HTTPSConnection('viacep.com.br')
    headers = {'Content-type': 'application/json'}

    conn.request('GET', '/ws/' + code + '/json/', 'null', headers)
    response = json.loads(conn.getresponse().read().decode())

    return response

