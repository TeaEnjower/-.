class Matrix:
    def __init__(self, elems):
        self.elems = elems

    def __str__(self):
        res_str = ''
        for row in self.elems:
            for elem in row:
                res_str += str(elem)
                res_str += '    '
            res_str = res_str[:-4] + '\n'
        return res_str[:-1]

    def size(self):
        return len(self.elems), len(self.elems[0])

    def __add__(self, other):
        if other.size() != self.size():
            return 'Матрицы сложить невозможно'
        return Matrix([[sum(i) for i in zip(self.elems[z], other.elems[z])] for z in range(self.size()[0])])

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            m1, n1, m2, n2 = *self.size(), *other.size()
            res = []
            for i in range(m1):
                res.append([0] * n2)
        else:
            return Matrix([[i * other for i in z] for z in self.elems])
        curr_summands = 0
        curr_sum = 0
        index_curr = 0
        for i in range(m1 * n1 * n2):
            curr_sum += self.elems[i // (n2 * n1)][i % n1] * other.elems[i % m2][(i // m2) % n2]
            curr_summands += 1
            if curr_summands == n1:
                res[index_curr // n2][index_curr % n2] = curr_sum
                curr_sum = 0
                curr_summands = 0
                index_curr += 1
        return Matrix(res)

    __rmul__ = __mul__

    @staticmethod
    def transposed(matrix):
        if len(matrix) != len(matrix[0]):
            return 'Транспонированию не подлежит'
        
        return Matrix([list(i) for i in zip(*matrix)])




class Vector1:
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
        return Vector1([0, 0, 0], coords)
    
    def __mul__(self, other):
        return sum(map(lambda x: x[0] * x[1], zip(self.coords, other.coords)))
    
    def get_length(self):
        return round(sum(map(lambda x: x**2, self.coords))**0.5, 5)
    
    def get_cos(self, other):
        return round((self * other)/(self.get_length() * other.get_length()), 4)
    

class Vector(Vector1, Matrix):
    def vector_mul(self, other):
        return Vector([0, 0, 0], [self.coords[1]*other.coords[2] - self.coords[2]*other.coords[1], self.coords[2]*other.coords[0] - self.coords[0]*other.coords[2], self.coords[0]*other.coords[1] - self.coords[1]*other.coords[0]])
    

vec1 = Vector([0, 0, 0], [1, 2, 3])
vec2 = Vector([0, 0, 0], [3, 4, 5])
print(vec1.vector_mul(vec2))
