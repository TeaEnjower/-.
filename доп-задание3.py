num = int(input(''))
n = int(input())
found = False
while found == False:
    for i in range(1, n+1):
        if i == num:
            num2 = i
            found = True
print('Your secret number =', num2)