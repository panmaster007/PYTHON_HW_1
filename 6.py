# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трёх цифр равно сумме последних трёх.
# т.е. билет с номером 385916 - счастливый, т.к. 3+8+6=9+1+6.
# Вам потребуется написть программу, которая проверяет счастливость билета.
# Пример: 385916 -> yes
#         123456 -> no
     

number = input('Введите номер билетика: ')
if int(number) > 99999 and int(number) <1000000:
   left_part = sum(map(int, number[:3]))
   right_part = sum(map(int, number[3:]))
   if left_part == right_part:
      print('Ваш билетик счастливый!!!')
   else:
      print('Ваш билетик обычный')
else:
   print('Вы ввели не шестизначный номер билетика либо вообще не число !!!')


