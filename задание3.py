def a(x, y):
    return (x >= 4 and y >= 3) or (x < 4 and y < 3 and x + y <= 0)


def b(x, y):
    return (3 - abs(x) >= 0) and (3 - abs(y) >= 0) and (x ** 2 + y ** 2 >= 9)


def c(x, y):
    return (0 <= x <= 5) and (0 <= y <= 5) and ((x - 5) ** 2 + (y - 5) ** 2 >= 25)


x = float(input('Введите координату x: '))
y = float(input('Введите координату y: '))

print ('')
print(a(x, y))
print(b(x, y))
print(c(x, y))


del x, y