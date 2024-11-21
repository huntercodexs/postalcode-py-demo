from clazz.clazz_postalcode_requests_simple import PostalCodeRequestsSimpleClazz
from library.library_postalcode_validator import PostalCodeValidatorLibrary

postalcode_library = PostalCodeValidatorLibrary()

def lambda_handler(event, context):
    postalcode_instance = PostalCodeRequestsSimpleClazz(postalcode_library=postalcode_library)
    return postalcode_instance.dispatch(code=event['postalcode'])
