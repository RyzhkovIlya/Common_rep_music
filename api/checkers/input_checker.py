<<<<<<< HEAD
from static.text import ERROR_TEXT
def input_checker(name):
    try:
        isinstance(name, (int, str))
        return name
    except:
        print(ERROR_TEXT)
=======
import pandas as pd

#s = input()

def input_checker(s):
    if (isinstance(s, (int, str))):
        return s

    else:
        return 'Ошибка, попробуйте ввести только в буквенном и числовом форматах'


print(input_checker(s))
>>>>>>> 1685e307cd677a811cb0213ec36609798aa3b19f
