## Немного о строках
"""Команды для работы со строками:"""
text = 'Съешь ещё этих Мягких французских булок'
#Определить количество символов в строке:
print(len(text))   #39
#Проверить наличие символа в строке (in):
print('ещё' in text)             #True
#Переводит в нижний регистр:
print(text.lower())            
#Переводит в верхний регистр:
print(text.upper())   
#Заменить слово на другое ,указываем сначало слово которое хотим заменить, потом на какое:
print(text.replace('ещё','ЕЩЁ')) 

### Срезы

"""- Мы представляем строку в виде массива символов. Значит мы можем обращаться к элементам по индексам.
- Отрицательное число в индексе — счёт с конца строки"""
text = 'Съешь ещё этих Мягких французских булок'
print(text[0])                           # c
print(text[1])                           # ъ
print(text[len(text)-1])                 # к
print(text[-1])                          # индексация с конца
print(text[-5])                          # б
print(text[:])                           # print(text) выводит весь текст
print(text[:2])                          # съ выводит 2 элемента (0 и 1)
print(text[len(text)-2:])                # ок
print(text[2:9])                         # ешь ещё
print(text[6:-18])                       # ещё этих мягких
print(text[0:len(text):6])               # сеикакл
print(text[::6])                         # сеикакл
text = text[2:9] + text[-5] + text[:2]   # ...

"""Список – пронумерованная, изменяемая коллекция
объектов произвольных типов
Списки: введение"""
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент