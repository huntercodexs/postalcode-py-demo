import json


class PostalCodeValidatorLibrary:

    @staticmethod
    def postalcode_validator(code:str):

        postalcode = code.replace("-", "").replace(".", "")

        if len(postalcode) == 8 and postalcode.isdigit():
            return postalcode

        else:
            raise ValueError(f"Invalid postalcode {postalcode}")

    @staticmethod
    def response_validator(resp):
        response = json.dumps(resp)
        print(f"RESPONSE-VALIDATOR: {response}")
        return response
