a = 5
b = 10
x = 'Hello world'
print(a)
print(b)
print(x)
print(a, ',', b, ',', x)            # 1 способ
print('{} ,{} , {}'.format(a, b, x))  # 2 способ
print(f'{a} ,{b} , {x}')            # 3 способ

list = [a, b, x]                      # список
print(list)

"""print('Put your number')
a = int(input())
print(a)"""          
                
a = 1.355
b = 3
c = round(a*b, 2)   # 2 указывает на количество цифр после запятой
print(c)

g = [1, 2, 3]
#print(g)
#print(not 2 in g)
is_odd = g[0] % 2 == 0
print(is_odd)


