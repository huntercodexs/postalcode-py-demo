import http.client

conn = http.client.HTTPSConnection('viacep.com.br')

headers = {'Content-type': 'application/json'}

conn.request('GET', '/ws/12090002/json/', 'null', headers)

response = conn.getresponse()
print(response.read().decode())

