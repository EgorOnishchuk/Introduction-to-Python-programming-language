def get_value(element):
    return input(f'Введите {element}. ')

def get_sequence():
    sequence = list()
    length = int(input('Введите количество чисел. '))
    for i in range(1, length + 1):
        sequence.append(int(input(f'Введите {i} число. ')))
    return sequence

def get_values(elements):
    return [i for i in input(f'Введите {elements}. ').split()]