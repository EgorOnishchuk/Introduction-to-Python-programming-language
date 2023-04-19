sequence_1, sequence_2 = list(), list()

length_1 = int(input('Введите количество чисел в первой последовательности. '))
for i in range(1, length_1 + 1):
    sequence_1.append(int(input(f'Введите {i} число. ')))
print(f'Первая последовательность - {sequence_1}')

length_2 = int(input('Введите количество чисел во второй последовательности. '))
for i in range(1, length_2 + 1):
    sequence_2.append(int(input(f'Введите {i} число. ')))
print(f'Вторая последовательность - {sequence_2}')

resulting_sequence = list(set(sequence_1).intersection(set(sequence_2)))
length_3 = len(resulting_sequence)

for i in range(length_3 - 1):
    min_index = i
    for j in range(i + 1, length_3):
        if resulting_sequence[j] < resulting_sequence[min_index]:
            min_index = j
    temporary = resulting_sequence[i]
    resulting_sequence[i] = resulting_sequence[min_index]
    resulting_sequence[min_index] = temporary

print(f'Последовательность без повторений в порядке возрастания - {resulting_sequence}')