import re

def validate_password(password):

    if not re.match(r'^[a-zA-Z0-9^$%@#&*]+$', password):
        return False

    if len(password) < 8:
        return False

    if not re.search(r'[a-z].*[a-z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    if len(set(re.findall(r'[^\w\s]', password))) < 3:
        return False

    return True

def run_tests():

    assert validate_password("rtG&3FG#Tr^e") == True
    assert validate_password("a^A1@*@1Aa") == True
    assert validate_password("oF^a1D@y5%e6") == True
    assert validate_password("enroi#$*rkdeR#$*092uwedchf34tguv394h") == True

    assert validate_password("пароль") == False
    assert validate_password("password") == False
    assert validate_password("qwerty") == False
    assert validate_password("lOngPa$$W0Rd") == False

    print("All tests passed!")

run_tests()