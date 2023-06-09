"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются
так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость 
введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо 
только русские буквы.
"""

russian_letters_values = {1: 'авеинорст', 2: 'дклмпу', 3: 'бгёья', 4: 'йы', 5: 'жзхцч', 8: 'шэю', 10: 'фщъ'}
english_letters_values = {1: 'aeioulnstr', 2: 'dg', 3: 'bcmp', 4: 'fhvwy', 5: 'k', 8: 'jx', 10: 'qz'}

language = input('Укажите, на каком языке будет вводиться слово. Для русского языка введите 0, для английского языка введите 1. ')
word = input('Введите слово строчными буквами. ')
points = 0

if language == '0':
    for i in word:
        for j in russian_letters_values:
            if i in russian_letters_values[j]:
                points += j
else:
    for i in word:
        for j in english_letters_values:
            if i in english_letters_values[j]:
                points += j

print(f'Стоимость слова {word} - {points}.')