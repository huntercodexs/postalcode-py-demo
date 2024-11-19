import http.client

from service.service_sample import ServiceSample
from service_main import ServiceMain

conn = http.client.HTTPSConnection('viacep.com.br')

headers = {'Content-type': 'application/json'}

conn.request('GET', '/ws/12090002/json/', 'null', headers)

response = conn.getresponse()
print(response.read().decode())

service_test = ServiceSample
service_test.test_service('Hello ')

service_main_test = ServiceMain
service_main_test.test_main('World')

