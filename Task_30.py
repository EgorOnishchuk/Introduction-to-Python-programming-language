from input import *

def get_arithmetical_progression(first_num, diffirence, length):
    arithmetical_progression = [first_num]

    for i in range(2, length + 1):
        arithmetical_progression.append(first_num + (i - 1) * diffirence)

    return arithmetical_progression

first_num = int(get_value('первый член прогрессии'))
diffirence = int(get_value('разность прогрессии'))
length = int(get_value('количество элементов прогрессии'))

print(f'Арифметическая прогрессия - {get_arithmetical_progression(first_num, diffirence, length)}')