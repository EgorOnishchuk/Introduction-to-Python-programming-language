"""Позволяет получать значения, введённые пользователем."""

def get_value(element):
    """Возвращает значение элемента, введённое пользователем."""
    return input(f'Введите {element}. ')

def get_sequence():
    """Возвращает список чисел, введённый пользователем."""
    sequence = list()
    length = int(input('Введите количество чисел. '))
    for i in range(1, length + 1):
        sequence.append(int(input(f'Введите {i} число. ')))
    return sequence

def get_values(elements):
    """Возвращает список значений элементов, введённый пользователем на одной строке через пробел."""
    return [i for i in input(f'Введите {elements}. ').split()]