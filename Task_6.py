"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом 
называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
"""

ticket_num = input('Введите шестизначный номер билета. ')
if int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2]) == int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5]):
    print(f'Билет {ticket_num} является счастливым.')
else:
    print(f'Билет {ticket_num} не является счастливым.')