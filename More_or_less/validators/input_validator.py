def input_validation(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False
