import numpy as np
import numpy.random as rand

x = np.random.randint(3, 10)
y = np.random.randint(3, 10)
a = np.random.randint(0, 2, (y, x))
P = 0

print(a)

for i in range(y):
    s = 0
for j in range(x):
    if a[i][j] == 0:
        s += 1
    print('На ', i+1 ,' ряду ', s, ' мест')

P += s
    
print('Мест всего', y*x)
print('Свободных мест', P)

i = int(input('Введите ряд '))
j = int(input('Введите место '))

if a[i-1][j-1] == 1: 
    print('Место занято')

else:
    print('Место свободно')