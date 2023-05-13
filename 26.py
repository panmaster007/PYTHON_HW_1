# Посчитать факториал (произведение 1 до N)
# и треугольное число (сумма чисел от 1 до N)
# для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def degree(a, b, c):
    if b != 0:
        c *= b
        b -= 1
    else:
        return c
    return  degree(a, b, c)

def summ(a, b, c):
    if b != 0:
        c += b
        b -= 1
    else:
        return c
    return summ(a, b, c)

x = int(input("Введите число N: "))
print(degree(2, x, 1))
print(summ(1, x, 0))
