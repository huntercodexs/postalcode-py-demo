from clazz.clazz_postalcode_http_client import PostalCodeHttpClientClazz
from library.library_postalcode_validator import PostalCodeValidatorLibrary

postalcode_library = PostalCodeValidatorLibrary()

def lambda_handler(event, context):
    postalcode_instance = PostalCodeHttpClientClazz(postalcode_library=postalcode_library)
    return postalcode_instance.dispatch(code=event['postalcode'])

