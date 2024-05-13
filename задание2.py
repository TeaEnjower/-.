import numpy as np
class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def __str__(self):
        S = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                S += str(self.matrix[i][j]) + '\t'
            S = S[:-1]
            S += '\n'
        return S[:-1]
    
    def size(self):
        return (len(self.matrix), len(self.matrix[0]))
    
    def __add__(self1, self2):
        if self1.size() != self2.size():
            raise ValueError("Размеры не совпадают")
            return None
        else:
            return Matrix(self1.matrix + self2.matrix)
        
    def __mul__(self1, self2):
        if type(self1) is int:
            return Matrix(self1 * self2.matrix)
        elif type(self2) is int:
            return Matrix(self2 * self1.matrix)
        elif len(self1.matrix[0]) != len(self2.matrix):
            raise ValueError("Матрицы нельзя умножить")
            return None
        else:
            return Matrix(np.dot(self1.matrix, self2.matrix))
    
    __rmul__ = __mul__
    
    def transposed(self):
        M = Matrix([])
        M.matrix = np.transpose(self.matrix)
        return M
m = Matrix( [ [0, 1, 2], [3, 4, 5], [6, 7, 8] ] )
n = Matrix( [ [1, 5, 9] ] )
print('Сумма двух одинаковых матриц m равна\n' + str(m + m))
print('Произведение матриц n и m равно\n' + str(n * m))
print('Матрица m - это\n' + str(m) + '\nа транспонированная ей - \n' + str(Matrix.transposed(m)))
print('Произведение матрицы m на число 2 равно\n' + str(2 * m))