import re


def move_validation(user_input):
    try:
        if int(user_input) > -1:
            return True
    except ValueError:
        return False
    return False


def name_validation(user_input):
    pattern = re.compile("[A-Z][a-zA-Z][^#&<>\"~;$^%{}?]{1,20}$")
    if pattern.match(user_input):
        return True
    else:
        return False
