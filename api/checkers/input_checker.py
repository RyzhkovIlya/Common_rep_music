from static.text import ERROR_TEXT
def input_checker(name):
    try:
        isinstance(name, (int, str))
        return name
    except:
        print(ERROR_TEXT)
