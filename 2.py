# Найдите сумму цифр трёхзначного числа
# Пример:  123 -> 6 (1 + 2 + 3)
#          100 -> 1 (1 + 0 + 0)

a = int(input('Введите трёхзначное число: '))
b = int(0)
if a > 99 and a < 1000:
   i = 0
   while i < 3:
     b += a % 10
     a = a // 10
     i = i + 1
else:
   print('Вы ввели не трёхзначное число либо вообще не число !!!') 
print(b)        