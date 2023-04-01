# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


"""k = int(input('Укажите сдвиг:'))
values = [1, 2, 3, 4, 5]
length = len(values)
#if length < k:
k = k % length -1
print(values)
#array.Length - k (это C#)
print(values[-k:] + values[:-k])"""

# Другой вариант

k = 3
list_1 = [1, 2, 3, 4, 5]
j = 0
list_2 = [0]*len(list_1)

for i in range(len(list_1)):
    j = (i + k) % len(list_1)
    list_2[i] = list_1[j]
    i += i

print(list_2)

