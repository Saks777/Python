### Управляющие конструкции: while-else
# Блок  else выполняется, когда основное тело цикла перестаёт работать.
# while condition:
#      # operator 1
#      # operator 2
# 		 # ...
# 		 # operator n
# else:
# 		 # operator n + 1 
# 		 # operator n + 2 
# 		 # ...
# 		 # operator n + m
# i = 0
# while i < 5:
#   # if i == 3:
#   #   break
#   i = i + 1
# else:
#   print('Пожалуй,хватит')
# print(i)  
  
# Вместо break используют метод флажка
n = int (input('Введите ваше число :')) # Код высчитывает минимальный делитель введенного числа
flag = True
i = 2
while flag:
  if n % i == 0: # Если остаток при делении числа n на i равен 0
    flag = False
    print(i)
  elif i > n // 2: # делить   числа не может превышать введенное число деленное на 0
    print(n)
    flag = False
  i += 1   