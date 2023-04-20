# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

from random import randint
N = int(input("\nВведите количество элементов в массиве: "))
X = int(input("\nВведите число ""X"": "))
lists = []
NumberMax = 0
NumberMin = 0
for el in range(0, N):
    i = randint(0, N)
    lists.append(i)
for i in range(0,len(lists)):
    if lists[i] == X+1:
        NumberMax = lists[i]
    elif lists[i] == X-1:
        NumberMin = lists[i]
print(f"\n{lists}")
if NumberMax == 0 and NumberMin == 0:
    print("Нет ближайших номеров.")
elif NumberMin == 0:
    print(f"\nБлижайшая цифра в списке к Х = {NumberMax}\n")
elif NumberMax == 0:
    print(f"\nБлижайшая цифра в списке к Х = {NumberMin}\n")
else:
    print(f"\nБлижайшая к X\nминимальная цифра = {NumberMin}\nмаксимальная цифра = {NumberMax}")