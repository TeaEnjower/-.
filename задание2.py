def a(x):
    return not (x and not x and 3 and 5) 


def b(x):
    return not a(x)


x = input('Enter smth: ')

print ('')
print (a(x))
print (b(x))


del x