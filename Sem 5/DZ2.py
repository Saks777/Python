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

# def second_max(tuple1: tuple = (), second_maximum: int = 0, max: int = 0):
#     x = int(input('Введите число: '))
#     if x > max:
#        second_maximum = max
#        max = x
#     elif x > second_maximum:
#         second_maximum = x

#     if x == 0:
#        tuple1 = (*tuple1, x)
#        print(f"Сформированный кортеж {tuple1}")
#        print(f"Второй максимум в кортеже это {second_maximum}")
#        return second_maximum
#     else:
#        tuple1 = (*tuple1, x)
#        return second_max(tuple1, second_maximum, max)

# a = second_max()
# print(a)