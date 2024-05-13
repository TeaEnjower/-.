a = input('Enter the element to be folded:')
c = 0

while a != 0:
    if a.isdigit():
        c += int(a)
        print('sum of number =', c)
        a = input('next one: ')
    else:
        for i in range(len(a)):
            b = ''
            if a[i].isdigit():
                b += a[i]
                c += int(b)
        print('sum of number =', c)
        a = input('next one: ')
        
print('sum of number =', c)