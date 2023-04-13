""" Задача №39. """

# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
""" Ввод:                       Вывод:"""
#  7                          3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1               (каждое число вводится с новой строки)


# n = int(input("Введите кол-во элементов 1-го множества :"))
# m = int(input("Введите кол-во элементов 2-го множества :"))

# array1 = []
# print("Введите элементы 1-го множества:")
# for i in range(n):
#   n1 =input()
#   array1.append(n1)
# print(f"Первое множество :", *array1)

# array2 = []
# print("Введите элементы 2-го множества:")
# for i in range(m):
#   n2 =input()
#   array2.append(n2)
# print(f"Второе множество :", *array2)

# array3 = []
# for i in array1:
#   if i not in array2:
#     array3.append(i)

# print(*(array3))

"""Упрощенный вариант"""
# a = [3, 1, 3, 4, 2, 4, 12]

# b = [4, 15, 43, 1, 15, 1]
# res = list(filter(lambda x: x not in b, a))
# print(res)
"""Другой вариант"""
# def input_number(msg: str) -> int:
# result = input(msg + ": ")
# while result.isdigit() == False:
# print("Введены некорректные данные. Попробуйте еще раз.")
# result = input(msg + ": ")
# return int(result)

# def main():
# n = input_number("Введите кол-во элементов первого множества")
# m = input_number("Введите кол-во элементов второго множества")
# arr1 = [input_number("Введите " + str(i+1) + " элемент 1го мн-ва" ) for i in range(n)]
# arr2 = [input_number("Введите " + str(i+1) + " элемент 2го мн-ва" ) for i in range(m)]
# print(set(arr1).difference(set(arr2)))


def input_num(message: str) -> int:

    input_error: bool = True

    while input_error:
        try:
            temp = int(input(message))
        except ValueError:
            print("Вы ввели не число!")
        else:
            input_error = False
        return temp


def input_list(message: str) -> list:

    temp_list = []
    for i in range(input_num('Please input size of ' + message + ': ')):
        temp_list.append(input_num(f'{i + 1} element of {message}: '))
    print('-' * 20)
    return temp_list


def input_num():
