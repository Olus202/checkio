import string


def find_message(text):
    result = ""
    for i in text:
        if i in string.ascii_uppercase:
            result += i
    return result
