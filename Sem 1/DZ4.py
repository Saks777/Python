"""Задача 8: Требуется определить, можно ли от шоколадки размером n
× m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).
3 2 4 -> yes
3 2 1 -> no"""

a = int(input('Введите 1 число :'))
b = int(input('Введите 2 число :'))
c = int(input('Введите 3 число :'))
if c <= b * a and (c % a == 0 or c % b == 0):
    print('Yes')
else:
    print('No')