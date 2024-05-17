class Vector:

    def __init__(self, coords1, coords2):
        if len(coords1) != 3 or len(coords2) != 3:
            raise ValueError('The dots must have 3 coordinates')
        self.coords1 = coords1
        self.coords2 = coords2
        self.coords = [coords2[i] - coords1[i] for i in range(3)]

    def __str__(self):
        return f'{self.coords}'

    def __add__(self, other):
        coords = [self.coords[i] + other.coords[i] for i in range(3)]
        return Vector([0, 0, 0], coords)
    
    def __mul__(self, other):
        return sum(map(lambda x: x[0] * x[1], zip(self.coords, other.coords)))
    
    def get_length(self):
        return round(sum(map(lambda x: x**2, self.coords))**0.5, 5)
    
    def get_cos(self, other):
        return round((self * other)/(self.get_length() * other.get_length()), 4)

v1 = Vector([0, 1, 0], [1, 2, 3])
v2 = Vector([1, 2, 3], [1, 5, -2])
print(f'Первый вектор: {v1}')
print(f'Второй вектор: {v2}')
print(f'Сумма векторов: {v1+v2}')
print(f'Скалярное произведение: {v1*v2}')
print(f'Длина вектора 1: {v1.get_length()}')
print(f'Косинус между двумя векторами: {v1.get_cos(v2)}')
