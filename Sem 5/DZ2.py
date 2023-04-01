# Урок 5. Рекурсия и алгоритмы
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4

def summ(a, b):

    if b == 0:
        return a

    return summ(a + 1, b - 1)

summa = summ(int(input('a:')), int(input('b:')))
print(f'sum is {summa}')