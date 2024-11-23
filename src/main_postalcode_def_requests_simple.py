from function.function_postalcode_requests_simple import dispatch_by_requests_simple


def lambda_handler(event, context):
    return dispatch_by_requests_simple(code=event['postalcode'])



