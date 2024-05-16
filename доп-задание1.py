a = int(input('Enter an integer:'))
n = a
k = len(str(n))                                     # number of characters per line
sum = 0

while k != 1:
    for i in range(1, k+1):
        sum = sum + n%10
        n = n//10
    n = sum
    print(sum)
    sum = 0
    k = len(str(n))
    
del a, n, k