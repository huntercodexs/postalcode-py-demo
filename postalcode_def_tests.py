from postalcode_def import requester

def test_postalcode_def_ok():

    event = {
        'postalcode': '12090002'
    }

    result = requester(event, None)
    assert result['cep'] == '12090-002'
    print('ok')

if __name__ == "__main__":
    test_postalcode_def_ok()

