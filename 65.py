#65
'''
VIERNES 13
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
'''

import datetime

def friday_13(input_year, input_month):
    x = datetime.datetime(int(input_year), int(input_month), 1)
    #print(x)
    y = x.weekday()
    # if the first day of the month is Sunday (0), then, there is a Friday 13
    if x.strftime("%w") == "0":
        return True
    else:
        return False

mm, yyyy = input("Provide a month MM and year YYYY, I will tell you if there is a Friday 13th in it: ").split()

print(friday_13(yyyy, mm))




