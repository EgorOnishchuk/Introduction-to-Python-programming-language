berries = list()
bushes = int(input('Введите количество кустов. '))

for i in range(1, bushes + 1):
    berries.append(int(input(f'Введите количество ягод на {i} кусте. ')))

print(f'Количество ягод на кустах - {berries}')

max_berries = 0
new_max_berries = 0
for i in range(bushes):
    if i + 1 == bushes:
        new_max_berries = berries[i] + berries[i - 1] + berries[0]
    else:
        new_max_berries = berries[i] + berries[i - 1] + berries[i + 1]
    if new_max_berries > max_berries:
        max_berries = new_max_berries

print(f'Максимально количество ягод, которое можно собрать за 1 заход - {max_berries}.')