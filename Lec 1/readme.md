Лекция 1. Знакомство с языком программирования  Python
   **Цель лекции:**

- познакомить студентов с принципами работы в Python и его синтаксисом.
**Почему для изучения выбран Python?**  

- Один из лидирующих языков программирования
- Высокоуровневый
- Впервые упоминается в 1991 v3.9
- Легчайший синтаксис
- Невысокий порог вхождения
- Востребованный на рынке
- Множество библиотек (базовых хватает)
- Популярен, хорошо оплачивается
- Кроссплатформенность
- Подходит для:
    - Веб-сервисов
    - ML, DataSciece, аналитики
    - Игр
    - Написания софта
- Интерпретируемый — для работы с Python на компьютер нужно установить интерпретатор

---

## Установка Python

1. Скачайте окружение [по ссылке](https://www.python.org/downloads/):
    - на macOS и Linux версия Python уже предустановлена, нужно её обновить;
    - на Windows — скачать и установить.
2. Перезагрузите компьютер.
3. Откройте терминал. Введите команду ***python***. Проверьте, что указана нужная версия Python (в нашем случае 3-я). Если версия старая, введите команду alias python=’python3’. Затем повторите команду python.
4. >>> print (’hello world’)

**Для Windows:** 

1. Откройте командную строку.
2. Введите команду *python*.
3. Откроется Miscrosoft Store, где вы сможете скачать нужную версию Python.
4. Установите Python.
5. Снова введите команду *python*.

Интерпретатор установлен!

Мы будем работать в **Visual Studio Code**.

- Чтобы работать было удобнее, установите расширение, которое будет подсвечивать синтаксис Python.
    - Extension → введите в поиске «python» → install.
    - В рабочем пространстве (Explorer) создайте папку с файлом для будущей программы.
    - print (’hello world’).

Как выполнить скрипт: 

- курсор в конце команды, правая кнопка мыши / выделить нужные строчки → run python file in terminal.

Если после выполнения команды в терминале остаются стрелочки >>>, нажмите **ctrl + Z**, чтобы выйти непосредственно в терминал. 

- Используйте стрелочку «запустить».

## Переменные в Python

### Базовые типы данных

| int | целые числа |
| --- | --- |
| float | число с плавающей запятой |
| boolean | логический тип данных (true/false) |
| list | список |
| str | строка |

### **Объявление переменной**

- название переменной = значение переменной (знак равенства обозначает присвоение)
- value = 2809
name = 'Sergey’


💡 **Python — язык с динамической типизацией.**


💡 Нельзя указать переменную, не присвоив ей какое-либо значение.

Но можно присвоить значение None и использовать переменную дальше по коду

### **Как узнать, какой тип данных содержится в переменной value?**

```python
print(type(value))
```

### **Как объявить строку?**

```python
s = ‘hello world'
print (s) #вывод строки
```

### **Как сделать комментарий?**

→ #

### **Использование одинарные или двойные кавычки внутри строки**

- используйте разные кавычки для объявления переменной и внутри строки:
    
    ```python
    s = ‘hello "world"'
    s = "hello 'world'"
    s = ‘hello \"world'
    ```
    

### **Интерполяция**

> Интерполяция — способ получить сложную строку из нескольких простых с использованием специальных шаблонов.
> 

Как вывести значения нескольких переменных: числа и строки?

```python
print (a,b,s)
print (a,'-'b,'-'s)
print ('{} - {} - {}'.format (a,b,s))
print (f'{a} - {b} - {s}')
```

### Логическая переменная

![Снимок экрана 2022-02-18 в 11.25.09.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/904c0102-504a-4a02-978f-d2239ce09f4c/Снимок_экрана_2022-02-18_в_11.25.09.png)

<aside>
💡 В Python нет массивов, но есть списки.

</aside>

![Снимок экрана 2022-02-18 в 11.26.43.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/13fabfe3-c107-44b0-ae30-c2f4e4067f48/Снимок_экрана_2022-02-18_в_11.26.43.png)

- Внутри списка можно использовать разные типы данных, но лучше использовать в одном списке данные одного типа (как и в массиве)

<aside>
💡 ****Неверно поставленный пробел сломает вашу программу!****

</aside>

![Снимок экрана 2022-02-18 в 11.30.16.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f58651dd-fcdb-4322-b843-025bec306e89/Снимок_экрана_2022-02-18_в_11.30.16.png)

![Снимок экрана 2022-02-18 в 11.33.21.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2c7611d5-a21d-4edd-b79d-71efdeff37dc/Снимок_экрана_2022-02-18_в_11.33.21.png)

---

## Операторы ввода и вывода данных

- **print()** — отвечает за вывод данных;
- **input()** — за ввод данных.

**Как показать сумму двух чисел?**

Так как по умолчанию мы работаем в строке, сумма двух переменных автоматически не посчитается. Для выполнения арифметических действий нужно указать тип данных **int**.

![Снимок экрана 2022-02-18 в 11.43.25.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9c535823-7058-4606-9d62-7307cb212e3a/Снимок_экрана_2022-02-18_в_11.43.25.png)

![Снимок экрана 2022-02-18 в 11.56.04.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d17acbbf-fa05-4beb-91f0-e62361301896/Снимок_экрана_2022-02-18_в_11.56.04.png)

---

## Арифметические операции

<aside>
💡 **Без них вы не напишете ни одной программы.**

</aside>

| Знак операции | Операция |
| --- | --- |
| + | Сложение |
| - | Вычитание |
| * | Умножение |
| / | Деление (по умолчанию в вещественных числах) |
| % | Остаток от деления |
| // | Целочисленное деление |
| ** | Возведение в степень |

### Приоритет арифметических операций

1. Возведение в степень (**)
2. Унарный минус (⊕)
    - обычно не пишется (обозначение положительного числа)
3. Унарный плюс (⊖)
    - инверсия — изменение знака числа на противоположный
4. Умножение (*)
5. Деление (/)
6. Целочисленное деление (//)
7. Остаток от деления (%)
8. Сложение (+)
9. Вычитание (-)

<aside>
💡 В Python нет лимита по хранению данных (нет ограничения по битам для хранения числа)

</aside>

### Округление числа

Можно указать количество знаков после запятой

```python
c = round(a*b, 5) #3,93693
```

### Сокращённые операции присваивания

```python
**iter = 2
iter += 3  # iter = iter + 3
iter -= 4  # iter = iter - 4
iter *= 5  # iter = iter * 5
iter /= 5  # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5  # iter = iter % 5
iter **= 5 # iter = iter ** 5** 
```

---

## Логические операции

| Знак операции | Операция |
| --- | --- |
| > | Больше |
| >= | Больше или равно |
| < | Меньше |
| <= | Меньше или равно |
| == | Равно (проверяет, равны ли числа) |
| != | Не равно (проверяет, не равны ли значения) |
| not | Не (отрицание) |
| and | И (конъюнкция) |
| or | Или (дизъюнкция) |

<aside>
💡 not, and, or — не путать с &, |, ^

</aside>

****Кое-что ещё: is, is not, in, not in****

```python
a =  1 > 4
print(a) # False

a =  1 < 4 and 5 > 2
print(a) # True

a =  1 == 2
print(a) # False

a =  1 != 2
print(a) # True
```

Можно сравнивать не только числовые значения, но и строки:

```python
a=’qwe’
b=’qwe'
print(a==b) # True
```

Списки сравниваются поэлементно:

```python
a=[1,2]
b=[1,2]
print(a==b )# True
```

В Python можно использовать тройные и даже четверные неравенства:

```python
a = 1 < 3 < 5 < 10
print (a) # True
```

Логические операции в списке:

1. Проверка, есть ли значение в списке.

```python
f = [1,2,3,4]
print (f)
print (2 in f) # True
print (not 2 in f) # False
```

1. Проверка, является ли элемент с заданным индексом чётным

```python
f = [1,2,3,4]
is_odd = f[0] % 2 == 0
print(is_odd) # False

is_odd = not f[0] % 2 == 0
print(is_odd) # False
```

---

## Управляющие конструкции: if, if-else

![Снимок экрана 2022-02-18 в 13.07.06.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7c9793d1-6150-474e-a7fd-8bafaa91b378/Снимок_экрана_2022-02-18_в_13.07.06.png)

В общем виде управляющие конструкции выглядят так:

<aside>
💡 Отступы очень важны!

</aside>

```python
if condition:
    # operator 1
    # operator 2
    # ...
    # operator n
else:
    # operator n + 1
    # operator n + 2
    # ...
    # operator n + m
```

Пример:

![Снимок экрана 2022-02-18 в 13.18.43.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/986981f1-341a-432c-a231-a2ef6d539d3f/Снимок_экрана_2022-02-18_в_13.18.43.png)

Ещё один вариант использования операторов if-else → в связке с elif

Проверяем первое условие, если оно не выполняется, проверяем второе и так далее.

```python
if condition1:
    # operator
elif condition2:
    # operator
elif condition3:
    # operator
else:
    # operator
```

```python
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)
```

---

## Управляющие конструкции: while и вариация while-else

### Управляющие конструкции: while

<aside>
💡 Цикл позволяет выполнить блок операторов какое-то количество раз.

</aside>

```python
while condition:
    # operator 1
    # operator 2
		# ...
		# operator n
```

```python
original = 23
 inverted = 0
 while original != 0:
     inverted = inverted * 10 + (original % 10)
     original //= 10
 print(inverted)
#32
```

### Управляющие конструкции: while-else

Блок else выполняется, когда основное тело цикла перестаёт работать.

```python
while condition:
     # operator 1
     # operator 2
		 # ...
		 # operator n
else:
		 # operator n + 1 
		 # operator n + 2 
		 # ...
		 # operator n + m
```

```python
original = 23
 inverted = 0
 while original != 0:
     inverted = inverted * 10 + (original % 10)
     original //= 10
 else:
     print('Пожалуй')
     print('хватит )')
 print(inverted)
 # Пожалуй
 # хватит )
 # 32
```

---

## Цикл for, range

### **for**

```python
for i in enumeration:
     # operator 1
		 # operator 2 
		 # ...
		 # operator n
```

```python
for i in 1, -2, 3, 14, 5:
     print(i)
# 1 
# -2 
# 3 
# 14 
# 5
```

В качестве итерируемого объекта может быть список

```python
list = [1,2,3,4,5]
for i in list:
		print(i**2)
# 1
# 4
# 9
# 16
# 25
```

### Range

- Range выдаёт значения из диапазона с шагом 1.
- Если указано только одно число — от 0 до заданного числа.
- Если нужен другой шаг, третьим аргументов можно задать приращение.

```python
r = range(5) 
r = range(2, 5)
r = range(-5, 0)
r = range(1, 10, 2)
r = range(100, 0, -20)
```

```python
r = range(100, 0, -20) # range(100, 0, -20)
 for i in r:
     print(i)
 # 100 80 60 40 20
 
for i in range(5):
     print(i)
 # 0 1 2 3 4
```

Можно использовать и со строками:

```python
 for i in 'qwerty':
     print(i)
 # q
 # w
 # e
 # r
 # t
 # y
```

Можно использовать вложенные циклы:

```python
 line = ""
 for i in range(5):
     line = ""
     for j in range(5):
         line += "*"
     print(line)
```

---

## Немного о строках

Команды для работы со строками:

```python
text = 'съешь ещё этих мягких французских булок'
```

1. Определить количество символов в строке:
    
    ```python
    print(len(text))   #39
    ```
    
2. Проверить наличие символа в строке (in):
    
    ```python
    print('ещё' in text)             #True
    ```
    
3. Проверить регистр:
    
    ```python
    print(text.islower())            #True
    ```
    
4. Заменить слово на другое :
    
    ```python
    print(text.replace('ещё','ЕЩЁ')) 
    ```
    

<aside>
💡 help(*название функции*) — встроенная справка о функции.

</aside>

### Срезы

- Мы представляем строку в виде массива символов. Значит мы можем обращаться к элементам по индексам.
- Отрицательное число в индексе — счёт с конца строки

```python
text = 'съешь ещё этих мягких французских булок'
 print(text[0])                           # c
 print(text[1])                           # ъ
 print(text[len(text)-1])                 # к
 print(text[-5])                          # б
 print(text[:])                           # print(text)
 print(text[:2])                          # съ
 print(text[len(text)-2:])                # ок
 print(text[2:9])                         # ешь ещё
 print(text[6:-18])                       # ещё этих мягких
 print(text[0:len(text):6])               # сеикакл
 print(text[::6])                         # сеикакл
 text = text[2:9] + text[-5] + text[:2]   # ...
```

---

## Списки: введение

> ****Список —**** пронумерованная, изменяемая коллекция объектов произвольных типов.
> 

Как можно задать список:

1. Задать все значения списка.
    
    ```python
     numbers = [1, 2, 3, 4, 5]
     print(numbers)               # [1, 2, 3, 4, 5]
    ```
    
2. Задать значения с помощью **range**.
    
    ```python
     numbers = list(range(1, 6))
     print(numbers)               # [1, 2, 3, 4, 5]
    ```
    

Работа с индексами:

```python
 numbers[0] = 10
 print(numbers)               # [10, 2, 3, 4, 5]

 for i in numbers:
     i *= 2
     print(i)                 # [20, 4, 6, 8, 10]
 print(numbers)               # [10, 2, 3, 4, 5]
```

Удаление и добавление элементов в строку:

```python
colors = ['red', 'green', 'blue']
 
for e in colors:
    print(e) # red green blue for e in colors:

for e in colors:
    print(e*2) # redred greengreen blueblue
 
 colors.append('gray') # добавить в конец
 print(colors == ['red', 'green', 'blue', 'gray']) # True
 
colors.remove('red') #del colors[0] # удалить элемент
```

---

## Функции

> Функция — это фрагмент программы, используемый многократно.
> 

В общем виде функция в Python выглядит так:

 def function_name(x):
     # body line 1
     # ...
     # body line n
     # optional return


 def f(x):
     return x**2

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
return

print(f(1))          # Целое
print(f(2.3))        # 23
print(f(28))         # None
print(type(f(1)))    # str
print(type(f(2.3)))  # int
print(type(f(28)))   # NoneType


