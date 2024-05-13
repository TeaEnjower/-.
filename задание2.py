x = int(input('Enter a number:'))

if x%4 == 0 and x%100 != 0:
    print ('Yes')
elif x%400 == 0:
    print ('Yes')
else:
    print ('No')

del x