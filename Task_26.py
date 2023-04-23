# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

from input import *

def raise_num_to_power(number, exponent):
    if exponent == 0 and number != 0:
        return 1
    
    if exponent == 0 and number == 0:
        return 0

    return number * raise_num_to_power(number, exponent - 1)


number = int(get_value('основание степени'))
exponent = int(get_value('показатель степени'))
print(f'Число {number} в степени {exponent} - {raise_num_to_power(number, exponent)}.')