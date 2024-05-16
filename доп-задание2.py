print('To abort the program, press "enter"')
print ('')

a = float(input('Введите число:'))
b = float(input('Введите число:'))

if a > b:
    max = a
    min = b
else:
    max = b
    min = a
try:
    while True:
        if a > max:
            max = a 
        elif a < min:
            min = a 
        a = float(input('Введите число:'))
        
except ValueError:
    pass

print ('')
print ('Maximum number:', max,'Minimum number:', min)


del a, b