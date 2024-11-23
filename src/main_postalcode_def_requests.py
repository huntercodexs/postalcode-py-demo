from function.function_postalcode_requests import dispatch_by_requests


def lambda_handler(event, context):
    return dispatch_by_requests(code=event['postalcode'])
