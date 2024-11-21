from clazz.clazz_postalcode_http_client import PostalCodeHttpClientClazz


def lambda_handler(event, context):
    return PostalCodeHttpClientClazz.dispatch(code=event['postalcode'])


