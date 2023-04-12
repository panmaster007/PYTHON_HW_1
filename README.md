# PYTHON_HW_1
n = input('Введите длинну шоколадки: ')
if (not n.isdigit() or int(n) < 1):
    exit('Введены не верные данные')
n = int(n)

m = input('Введите ширину шоколадки: ')
if (not m.isdigit() or int(m) < 1):
    exit('Введены не верные данные')
m = int(m)

k = input('Сколько хотите отломить?: ')
if (not k.isdigit() or int(k) < 1):
    exit('Введены не верные данные')
k = int(k)

if k < n * m:
    if k % n == 0 or k % m == 0:
        print('Да')
    else:
        print('Нет')
else:
    print('Не жадничай')

===============================================

number = input('Введите шестизначный номер билета: ')

if int(number) < 99999 or int(number) > 1000000:
    print('Вы ввели не шестизначный номер')

else:
    first_part = sum(map(int, number[:3]))
    second_part = sum(map(int, number[3:]))
    if first_part == second_part:
        print('Yes')
    else:
        print('No')
        
        =========================================================
        
part_n = int(input('Сколько долек в длину? '))
part_m = int(input('Сколько долек в ширину? '))
part_k = int(input('Сколько долек нужно отломить? '))

if (part_k % part_n == 0 or part_k % part_m == 0) and part_k <= part_n * part_m:
    print('YES')
else:
    print('NO')
    
    =======================================================
    
    
