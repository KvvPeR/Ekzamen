#№1
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [i for i in a if i<5]
#print(b)
#№2
#import random
#import math
#q = int(input('Введите число'))
#i = [random.randint(0, 16) for i in range(q)]
#print(i)
#a = math.prod(i)
#print(a)
#№3
#numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
#for a in numbers:
#    if a%2==0:
#         print(a)
#   elif a==237:
#        break
#№4
#age = int(input('Your age'))
#print(age)
#if age<2:
#    print('Младенец')
#elif 1<age<4:
#    print('Малыш')
#elif 3<age<13:
#    print('Ребёнок')
#elif 12<age<20:
#    print('Подросток')
#elif 20<age<65:
#   print('Взрослый')
#elif age>=65:
#        print('Пожилой')
#№5
#users = ['user1','user2','user3','user4','user5','user6','user7']
#verified = [i for i in users]
#print('User verified: ',verified)
#№6
#eat = ['pizza', 'falafel', 'carrot cake']
#friend_eat = ['pizza', 'falafel', 'carrot cake']
#a = input('Vvedite icecream')
#friend_eat.append(a)
#for i in friend_eat:
#    print(f"My Friend like: {i}")
#print(f"I like: {eat}")
#№7
#import math
#lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
#for i in lst:
#    if i%3==0 and i<30:
#        print(i)
#items = lst[0] + lst[1] + lst[2] + lst[3] + lst[6] + lst[7] + lst[9] + lst[10] + lst[12]
#print(items)
#№8
#Dictionary = {'a': 2, 'b': 4, 'c': 6, 'd': 8}
#for i in Dictionary.values():
#    if i>2:
#        print(i)
#№9
a = [1,2,3,4,5,6]
b = ['a','b','c','d','e','f']
#№10


#№11
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic1 = [dic.values() for i in dic.values() if i%2==0 : i='even' else : i='odd' ]
print(dic1)
#№12      
#import random
#n = int(input('Vvedite kol-vo strochek'))
#m = int(input('Vvedite kol-vo stolbikov'))
#matrix = [[random.randint(0,9) for w in range(m)] for q in range(n)]
#for a in matrix:
#        print(a)
#diagonal = [matrix[w][q] for w in range(n) for q in range(m) if w==q]
#print('Главная диагональ ===>',diagonal)
#k = int(input('Номер строки'))
#p = int(input('Номер столбца'))
#item = [matrix[k-1][w] for w in range(m)]
#item1 = [matrix[q][p-1] for q in range(n)]
#print(item)
#print(item1)
#r = int(input('Номер строки элемента'))
#t = int(input('Номер столбца элемента'))
#item2 = matrix[r-1][t-1]
#print(item2)
        
        
