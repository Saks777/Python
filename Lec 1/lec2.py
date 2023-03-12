### Управляющие конструкции: while
# Цикл позволяет выполнить блок операторов какое-то количество раз.
# while condition:
#     # operator 1
#     # operator 2
# 		# ...
# 		# operator n
n = 423    # Сложить сумму всех цифр
summa = 0
while n > 0:
  x = n % 10
  summa = summa + x
  n = n // 10
print(summa) # Ответ 9