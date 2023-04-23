from input import *

def get_numbers_sum(num_1, num_2):
    if num_2 == 0:
        return num_1
    
    return get_numbers_sum(num_1 + 1, num_2 - 1)


numbers = get_values('числа')
num_1 = int(numbers[0])
num_2 = int(numbers[1])

print(f'Сумма чисел {num_1} и {num_2} - {get_numbers_sum(num_1, num_2)}.')