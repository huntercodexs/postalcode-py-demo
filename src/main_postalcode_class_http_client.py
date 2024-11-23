from library.library_postalcode_handle_api import PostalCodeHandleApiLibrary
from library.library_postalcode_validator import PostalCodeValidatorLibrary

postalcode_library = PostalCodeValidatorLibrary()
postalcode_requester = PostalCodeHandleApiLibrary()

def lambda_handler(event, context=None, mock=None):

    if mock is not None:
        postalcode_instance = PostalCodeHttpClientClazz(
            postalcode_lib=mock['postalcode_lib'],
            postalcode_req=mock['postalcode_req']
        )

    else:
        postalcode_instance = PostalCodeHttpClientClazz(
            postalcode_lib=postalcode_library,
            postalcode_req=postalcode_requester
        )

    return postalcode_instance.dispatch(code=event['postalcode'])


class PostalCodeHttpClientClazz:

    def __init__(
        self,
        postalcode_lib: PostalCodeValidatorLibrary = postalcode_library,
        postalcode_req: PostalCodeHandleApiLibrary = postalcode_requester
    ):
        self.__postalcode_lib = postalcode_lib
        self.__postalcode_req = postalcode_req

    def dispatch(self, code:str):
        code = self.__postalcode_lib.postalcode_validator(code=code)
        response = self.__postalcode_req.postalcode_requester(code=code)
        return response
