import http.client
from time import sleep

from clazz.clazz_postalcode_http_client import PostalCodeHttpClientClazz
from clazz.clazz_postalcode_requests import PostalCodeRequestsClazz
from clazz.clazz_postalcode_requests_simple import PostalCodeRequestsSimpleClazz
from handle.handle_postalcode_http_client import PostalCodeHttpClientHandleAPI
from handle.handle_postalcode_requests import PostalCodeRequestsHandleAPI
from handle.handle_postalcode_requests_simple import PostalCodeRequestsSimpleHandleAPI
from library.library_postalcode_validator import PostalCodeValidatorLibrary
from service.service_sample import ServiceSample
from main_service import ServiceMain
from function.function_postalcode_http_client import dispatch_by_http_client
from function.function_postalcode_requests import dispatch_by_requests
from function.function_postalcode_requests_simple import dispatch_by_requests_simple

tt=1

conn = http.client.HTTPSConnection('viacep.com.br')
headers = {'Content-type': 'application/json'}
conn.request('GET', '/ws/12090002/json/', 'null', headers)
response = conn.getresponse()
print('SCRIPT')
print(response.read().decode())
sleep(tt)

postalcode_library = PostalCodeValidatorLibrary()

postalCodeHttpClientClazz = PostalCodeHttpClientClazz(postalcode_library=postalcode_library)
print('PostalCodeHttpClientClazz')
print(postalCodeHttpClientClazz.dispatch(code='12070180'))
sleep(tt)

postalCodeRequestsClazz = PostalCodeRequestsClazz(postalcode_library=postalcode_library)
print('PostalCodeRequestsClazz')
print(postalCodeRequestsClazz.dispatch(code='12070020'))
sleep(tt)

postalCodeRequestsSimpleClazz = PostalCodeRequestsSimpleClazz(postalcode_library=postalcode_library)
print('PostalCodeRequestsSimpleClazz')
print(postalCodeRequestsSimpleClazz.dispatch(code='12009020'))
sleep(tt)

dispatch_by_http_client = dispatch_by_http_client(code='12090001')
print('dispatch_by_http_client')
print(dispatch_by_http_client)
sleep(tt)

dispatch_by_requests = dispatch_by_requests(code='12070010')
print('dispatch_by_requests')
print(dispatch_by_requests)
sleep(tt)

dispatch_by_requests_simple = dispatch_by_requests_simple(code='12090002')
print('dispatch_by_requests_simple')
print(dispatch_by_requests_simple)
sleep(tt)

postalCodeHttpClientHandleAPI = PostalCodeHttpClientHandleAPI(postalcode_library=postalcode_library)
print('PostalCodeHttpClientHandleAPI')
print(postalCodeHttpClientHandleAPI.dispatch(code='12070010'))
sleep(tt)

postalCodeRequestsHandleAPI = PostalCodeRequestsHandleAPI(postalcode_library=postalcode_library)
print('PostalCodeRequestsHandleAPI')
print(postalCodeRequestsHandleAPI.dispatch(code='12070010'))
sleep(tt)

postalCodeRequestsSimpleHandleAPI = PostalCodeRequestsSimpleHandleAPI(postalcode_library=postalcode_library)
print('PostalCodeRequestsSimpleHandleAPI')
print(postalCodeRequestsSimpleHandleAPI.dispatch(code='12070010'))
sleep(tt)

service_test = ServiceSample
service_test.print_service_sample_message('Hello')

service_main_test = ServiceMain
service_main_test.print_service_main_message('World')