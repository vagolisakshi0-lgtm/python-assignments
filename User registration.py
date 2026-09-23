def check_length(username):
    return 5 <= len(username) <= 15


def check_characters(username):
    for ch in username:
        if not (ch.isalnum() or ch == "_"):
            return False
    return True


def validate_username(username):
    if username == "":
        return False

    if not username[0].isalpha():
        return False

    if not check_length(username):
        return False

    if not check_characters(username):
        return False

    return True


username = input("Enter username: ")

if validate_username(username):
    print("Valid username")
else:
    print("Invalid username")
