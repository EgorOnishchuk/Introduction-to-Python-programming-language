number = int(input('Введите число. '))
exponent = 0

while(2 ** exponent <= number):
    print(2 ** exponent, end = ' ')
    exponent += 1