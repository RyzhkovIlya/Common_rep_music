<<<<<<< HEAD
=======
from webapp.static.text import ERROR_TEXT
>>>>>>> 65518692ba2e6f3f635b81c7325de2703e8f2774
def input_checker(name):
    try:
        isinstance(name, (int, str))
        return name
    except:
        print('error')
