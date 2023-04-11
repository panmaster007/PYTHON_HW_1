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
