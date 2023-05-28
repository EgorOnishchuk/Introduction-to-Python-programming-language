"""Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько
легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в 
каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
"""

import input

def is_poem_rhythmic(poem):
    vowels = 'аеёиоуыэюя'
    phrases_vowels = list()
    phrases = poem.split()

    for i in phrases:
        count= 0
        for j in i:
            if j in vowels:
                count += 1
        phrases_vowels.append(count)

    for i in phrases_vowels:
        if phrases_vowels[0] != i:
            return False
        
    return True


poem = input.get_value('стихотворение')
if is_poem_rhythmic(poem):
    print('Парам пам-пам.')
else:
    print('Пам парам.')