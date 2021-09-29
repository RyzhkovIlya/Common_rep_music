import pandas as pd

#s = input()

def input_checker(s):
    if (isinstance(s, (int, str))):
        return s

    else:
        return 'Ошибка, попробуйте ввести только в буквенном и числовом форматах'


print(input_checker(s))
