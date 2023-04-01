"""Задача №23. Решение в группах"""
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# Вариант с кортежами
"""l = [0, -1, 5, 2, 3]
def big_counter(list):
    result = []
    for i in range(len(list)-1):
        if list[i] < list[i + 1]:
            result.append(f"{list[i]} < {list[i + 1]}")
    result = tuple(result)
            
    print(result)
big_counter(l)"""

# Другой вариант без кортежей
source = [0, -1, 5, 2, 3]
count = 0
idx = 0
while idx < len(source) - 1:
    idx += 1
    if source[idx - 1] < source[idx]:
        count += 1
print(count)