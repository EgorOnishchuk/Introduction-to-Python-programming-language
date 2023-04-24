from input import *

def get_indices(sequence, range_first_num, range_last_num):
    indices = list()
    length = len(sequence)

    for i in range(length):
        if range_first_num <= sequence[i] <= range_last_num:
            indices.append(i)

    return indices

sequence = get_sequence()
elements = get_values('первое и последнее значения диапазона')
range_first_num = int(elements[0])
range_last_num = int(elements[1])

print(f'Индексы элементов - {get_indices(sequence, range_first_num, range_last_num)}')