from function.function_postalcode_http_client import dispatch_by_http_client


def lambda_handler(event, context):
    return dispatch_by_http_client(code=event['postalcode'])
