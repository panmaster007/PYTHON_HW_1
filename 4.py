# Петя, Катя и Серёжа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребёнок, если известно,
# что Петя и Серёжа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Серёжа вместе?
# Пример: 6  ->  1  4  1
#         24 ->  4  16 4
#         60 ->  10 40 10

coll = int(input('Введите количество всех журавликов: '))
if coll % 6 == 0:
   petya = int(coll / 6)
   katya = int(coll / 6  * 4)
   sereza = int(coll / 6)
else:
   print('Вы ввели не верное количество журавликов либо вообще не число !!!') 
print(f"{coll} -> {petya} {katya} {sereza}")
