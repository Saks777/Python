# Управляющие конструкции: while
# Цикл позволяет выполнить блок операторов какое-то количество раз.
# while condition:
#     # operator 1
#     # operator 2
# 		# ...
# 		# operator n
"""n = 423    # Сложить сумму всех цифр
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa)  # Ответ 9"""
# Перевернуть цифры
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10

print(inverted)


# Другой вариант
"""number = int(input("Введите трехзначное положительное число: "))

if 99 < number < 1000:
    houndreds = number // 100
    tens = number // 10 % 10
    units = number % 10
    result = houndreds + tens + units
    print(f"{number} -> {result} ({houndreds} + {tens} + {units})")

else:
    print("Введено число, не удовлетворяющее условию!")"""
