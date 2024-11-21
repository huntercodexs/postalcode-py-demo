from clazz.clazz_postalcode_requests_simple import PostalCodeRequestsSimpleClazz


def lambda_handler(event, context):
    return PostalCodeRequestsSimpleClazz.dispatch(code=event['postalcode'])


