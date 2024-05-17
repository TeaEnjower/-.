class Polynomial:
    def __init__(self, degree, coefficients):
        self.degree = degree
        self.coefficients = coefficients

    def calculate(self, x):
        result = 0
        for i in range(self.degree + 1):
            result += self.coefficients[i] * (x ** i)
        return result

    def add(self, other):
        new_degree = max(self.degree, other.degree)
        new_coefficients = [0] * (new_degree + 1)
        for i in range(self.degree + 1):
            new_coefficients[i] += self.coefficients[i]
        for i in range(other.degree + 1):
            new_coefficients[i] += other.coefficients[i]
        return Polynomial(new_degree, new_coefficients)

    def subtract(self, other):
        new_degree = max(self.degree, other.degree)
        new_coefficients = [0] * (new_degree + 1)
        for i in range(self.degree + 1):
            new_coefficients[i] += self.coefficients[i]
        for i in range(other.degree + 1):
            new_coefficients[i] -= other.coefficients[i]
        return Polynomial(new_degree, new_coefficients)

    def multiply(self, other):
        new_degree = self.degree + other.degree
        new_coefficients = [0] * (new_degree + 1)
        for i in range(self.degree + 1):
            for j in range(other.degree + 1):
                new_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(new_degree, new_coefficients)

    def display(self):
        print("Степень многочлена:", self.degree)
        print("Коэффициенты многочлена:", self.coefficients)



p1 = Polynomial(2, [1, 2, 3])
p2 = Polynomial(1, [2, 1])

p1.display()
p2.display()

print("Значение многочлена p1 при x=2:", p1.calculate(2))
print("Значение многочлена p2 при x=3:", p2.calculate(3))

p3 = p1.add(p2)
p3.display()

p4 = p1.subtract(p2)
p4.display()

p5 = p1.multiply(p2)
p5.display()