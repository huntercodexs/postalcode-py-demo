from clazz.clazz_postalcode_requests import PostalCodeRequestsClazz


def lambda_handler(event, context):
    return PostalCodeRequestsClazz.dispatch(code=event['postalcode'])


