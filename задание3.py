x = float (1 + 2 + 3 + 4 + 5)
y = float (x/5)
n = float (input ('Enter a number:'))
i = 5

while n!=0:
    i = i + 1
    x = x + n
    y = x/i
    print ('The average value of these 5 numbers is', '%.5f'%y)
    n = float (input ('Enter a number:'))
        
if n == 0 : print ('Your session is over')


del x, y, n, i