#Посчитать количество встречающихся одинаковых значений

list_1 = "sfdsfdsfsfsfgggeeeesdfsf"
dict_2 = {}
j = 0
for i in list_1:
    dict_2[i] = j
    
for i in list_1:
    if i in dict_2:
        dict_2[i] = dict_2[i] + 1
print(f'Одинаковых значений = {dict_2}')