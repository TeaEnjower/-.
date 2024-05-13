class Common:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f'{self.a if self.a != 0 else ""}{"+" if self.b>0 else ""}{"" if (self.b == 0 and self.a != 0) else self.b}{"i" if self.b != 0 else ""}'

class Complex(Common):
    def __add__(self, other):
        return Complex(self.a+other.a, self.b+other.b)
    
    def __sub__(self, other):
        return Complex(self.a-other.a, self.b-other.b)
    
    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b, self.b*other.a + self.a*other.b)
    
    def __floordiv__(self, other):
        return Complex(round((self.a*other.a + self.b*other.b)/(other.b**2 + other.a**2), 3), round((other.a*self.b - self.a*other.b)/(other.a**2 + other.b**2), 3))

    
class Double(Common):
    def __add__(self, other):
        return Double(self.a+other.a, self.b+other.b)
    
    def __sub__(self, other):
        return Double(self.a-other.a, self.b-other.b)
    
    def __mul__(self, other):
        return Double(self.a*other.a + self.b*other.b, self.b*other.a + self.a*other.b)
    
    def __floordiv__(self, other):
        return Double(round((self.a*other.a + self.b*other.b)/(other.a**2 - other.b**2), 3), round((other.a*self.b - self.a*other.b)/(other.a**2 - other.b**2), 3))

    
class Dual(Common):
    def __add__(self, other):
        return Dual(self.a+other.a, self.b+other.b)
    
    def __sub__(self, other):
        return Dual(self.a-other.a, self.b-other.b)
    
    def __mul__(self, other):
        return Dual(self.a*other.a, self.b*other.a + self.a*other.b)
    
    def __floordiv__(self, other):
        return Dual(round((self.a)/(other.a), 3), round((self.a*other.b + other.a*self.b)/(other.a**2), 3))



complex1 = Complex(2, 3211)
complex2 = Complex(3, -123)
print(complex1)
print(complex2)

print(complex1 + complex2)
print(complex2-complex1)
print(complex1 * complex2)
print(complex1 // complex2)

print('---------')

double1 = Double(2, 3211)
double2 = Double(3, -123)
print(double1)
print(double2)

print(double1 + double2)
print(double1-double2)
print(double1 * double2)
print(double1 // double2)

print('----------')

dual1 = Dual(2, 3211)
dual2 = Dual(3, -123)
print(dual1)
print(dual2)

print(dual1 + dual2)
print(dual1-dual2)
print(dual1 * dual2)
print(dual1 // dual2)