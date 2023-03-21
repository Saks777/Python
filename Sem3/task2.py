#Задача №21. Решение в группах
#Напишите программу для печати всех уникальных
#значений в словаре.
#Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
#":" S007 "}]
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}"""

"""words = [ {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {"VIII":" S007 "}
]

def unic_printer(list_data):
    result = set()
    for item in list_data:
        result.add(*item.values())
    print(result)
    
unic_printer(words)"""

# Другой вариант
"""dictionary = [{"V": "S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
unique = {''}
unique.clear()
for item in dictionary:
  print(item)
for temp in item:
  unique.add(f'{item[temp]}')
print(unique)"""

# Другой вариант со .strip() и replace
dict1 = [ {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
{"VIII":" S007 "} ]
list1 = [0]*len(dict1)
i = 0
for element in dict1:
    for key in element.keys():
        list1[i] = element[key]
        i+=1
print(f'Дано :' + str(list1))
#list1 = [i.replace(' ', '') for i in list1] # replace заменил ' ' на ''
list1 = [i.strip() for i in list1] # .strip() вместо replace
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(f'Ответ :' + str(list2))             





  
