class Option:
    def __init__(self, name, *args):
        self.name = name
        if self.name == 'Triangle perimeter':
            self.descr = self.get_triangle_perimeter(*args)
        elif self.name == 'Rectangle perimeter':
            self.descr = self.get_rectangle_perimeter(*args)
        elif self.name == 'Circle perimeter':
            self.descr = self.get_circle_perimeter(*args)
        elif self.name == 'Triangle square':
            self.descr = self.get_triangle_square(*args)
        elif self.name == 'Rectangle square':
            self.descr = self.get_rectangle_square(*args)
        elif self.name == 'Circle square':
            self.descr = self.get_circle_square(*args)

    def __str__(self):
        return f'{self.descr}'

    @staticmethod
    def get_triangle_perimeter(fst, snd, trd):
        return round(fst + snd + trd, 5)
    
    @staticmethod
    def get_rectangle_perimeter(fst, snd, trd, frth):
        return round(fst + snd + trd + frth, 5)
    
    @staticmethod
    def get_circle_perimeter(radius):
        return round(2 * math.pi * radius, 5)
    
    @staticmethod
    def get_triangle_square(fst, snd, trd):
        half_per = (fst + snd + trd) / 2
        return round((half_per * (half_per - fst) * (half_per - snd) * (half_per - trd)) ** 0.5, 5)  # формула Герона
    
    @staticmethod
    def get_rectangle_square(fst, snd):
        return round(fst * snd, 5)
    
    @staticmethod
    def get_circle_square(radius):
        return round(2 * math.pi * radius, 5)
import matplotlib.pyplot as plt
import math
import numpy as np

class GeoGebra:
    def __init__(self, coords):
        self.coords = coords
        self.perimeter = self.calc_perimeter()
        self.square = self.calc_square()

    def paint(self):
        x = [i for i in map(lambda p: p[0], self.coords)] + [self.coords[0][0]]
        y = [i for i in map(lambda p: p[1], self.coords)] + [self.coords[0][1]]
        plt.plot(x, y)
        plt.show()

class Triangle(GeoGebra):
    def __init__(self, coords):
        self._fst = ((coords[0][0] - coords[2][0]) ** 2 + (
                    coords[0][1] - coords[2][1]) ** 2) ** 0.5
        self._snd = ((coords[0][0] - coords[1][0]) ** 2 + (
                    coords[0][1] - coords[1][1]) ** 2) ** 0.5
        self._trd = ((coords[1][0] - coords[2][0]) ** 2 + (
                    coords[1][1] - coords[2][1]) ** 2) ** 0.5
        super().__init__(coords)
        
    def calc_perimeter(self):
        return Option('Triangle perimeter', self._fst, self._snd, self._trd)

    def calc_square(self):
        return Option('Triangle square', self._fst, self._snd, self._trd)

    

class Rectangle(GeoGebra):
    """Порядок записи координат важен!"""
    def __init__(self, coords):
        self._fst = ((coords[0][0] - coords[1][0]) ** 2 + (coords[0][1] - coords[1][1]) ** 2) ** 0.5
        self._snd = ((coords[0][0] - coords[3][0]) ** 2 + (coords[0][1] - coords[3][1]) ** 2) ** 0.5
        self._trd = ((coords[2][0] - coords[3][0]) ** 2 + (coords[2][1] - coords[3][1]) ** 2) ** 0.5
        self._frth = ((coords[2][0] - coords[1][0]) ** 2 + (coords[2][1] - coords[1][1]) ** 2) ** 0.5
        super().__init__(coords)
        self.is_rectangle = self.check_rectangle()
        if not self.is_rectangle:
            print('Это не прямоугольник! Но все же это четырехугольник')
    
    def check_rectangle(self):
        diag1 = ((self.coords[0][0] - self.coords[2][0]) ** 2 + (self.coords[0][1] - self.coords[2][1]) ** 2) ** 0.5
        diag2 = ((self.coords[1][0] - self.coords[3][0]) ** 2 + (self.coords[1][1] - self.coords[3][1]) ** 2) ** 0.5
        return diag1 == diag2

    def calc_perimeter(self):
        return Option('Rectangle perimeter', self._fst, self._snd, self._trd, self._frth)

    def calc_square(self):
        return Option('Rectangle square', self._fst, self._snd)

class Circle(GeoGebra):
    def __init__(self, coord, radius):
        self.coord = coord
        self.radius = radius
        self.perimeter = self.calc_perimeter()
        self.square = self.calc_square()

    def calc_perimeter(self):
        return Option('Circle perimeter', self.radius)
    
    def calc_square(self):
        return Option('Circle square', self.radius)
    
    def paint(self):
        theta = np.linspace( 0 , 2 * np.pi , 150 )

        a = self.radius * np.cos( theta ) + self.coord[0]
        b = self.radius * np.sin( theta ) + self.coord[1]
        figure, axes = plt.subplots( 1 )
        
        axes.plot( a, b )
        axes.set_aspect( 1 )
        
        plt.show()


triangle1 = Triangle([(41, 6), (5, 5), (2, 32)])
print(triangle1.perimeter)
print(triangle1.square)
triangle1.paint()

rectangle1 = Rectangle([(2, 2), (4, 2), (4, 1), (2, 1)])
print(rectangle1.perimeter)
print(rectangle1.square)
rectangle1.paint()

circle1 = Circle((1, 0), 2)
print(circle1.perimeter)
print(circle1.square)
circle1.paint()


#часть 2

import matplotlib.pyplot as plt
import math
import numpy as np

class GeoGebra:
    def __init__(self, coords):
        self.coords = coords
        self.perimeter = self.calc_perimeter()
        self.square = self.calc_square()

    def paint(self):
        x = [i for i in map(lambda p: p[0], self.coords)] + [self.coords[0][0]]
        y = [i for i in map(lambda p: p[1], self.coords)] + [self.coords[0][1]]
        plt.plot(x, y)
        plt.show()

class Triangle(GeoGebra):
    def calc_perimeter(self):
        self._fst = fst = ((self.coords[0][0] - self.coords[2][0]) ** 2 + (
                    self.coords[0][1] - self.coords[2][1]) ** 2) ** 0.5
        self._snd = snd = ((self.coords[0][0] - self.coords[1][0]) ** 2 + (
                    self.coords[0][1] - self.coords[1][1]) ** 2) ** 0.5
        self._trd = trd = ((self.coords[1][0] - self.coords[2][0]) ** 2 + (
                    self.coords[1][1] - self.coords[2][1]) ** 2) ** 0.5
        return round(fst + snd + trd, 5)

    def calc_square(self):
        fst = self._fst
        snd = self._snd
        trd = self._trd
        half_per = (fst + snd + trd) / 2
        return round((half_per * (half_per - fst) * (half_per - snd) * (half_per - trd)) ** 0.5, 5)  # формула Герона

    

class Rectangle(GeoGebra):
    """Порядок записи координат важен!"""
    def __init__(self, coords):
        super().__init__(coords)
        self.is_rectangle = self.check_rectangle()
        if not self.is_rectangle:
            print('Это не прямоугольник! Но все же это четырехугольник')
    
    def check_rectangle(self):
        diag1 = ((self.coords[0][0] - self.coords[2][0]) ** 2 + (self.coords[0][1] - self.coords[2][1]) ** 2) ** 0.5
        diag2 = ((self.coords[1][0] - self.coords[3][0]) ** 2 + (self.coords[1][1] - self.coords[3][1]) ** 2) ** 0.5
        return diag1 == diag2

    def calc_perimeter(self):
        self._fst = fst = ((self.coords[0][0] - self.coords[1][0]) ** 2 + (self.coords[0][1] - self.coords[1][1]) ** 2) ** 0.5
        self._snd = snd = ((self.coords[0][0] - self.coords[3][0]) ** 2 + (self.coords[0][1] - self.coords[3][1]) ** 2) ** 0.5
        self._trd = trd = ((self.coords[2][0] - self.coords[3][0]) ** 2 + (self.coords[2][1] - self.coords[3][1]) ** 2) ** 0.5
        self._frth = frth = ((self.coords[2][0] - self.coords[1][0]) ** 2 + (self.coords[2][1] - self.coords[1][1]) ** 2) ** 0.5
        return round(fst + snd + trd + frth, 5)


    def calc_square(self):
        return round(self._fst * self._snd, 5)

class Circle(GeoGebra):
    def __init__(self, coord, radius):
        self.coord = coord
        self.radius = radius
        self.perimeter = self.calc_perimeter()
        self.square = self.calc_square()

    def calc_perimeter(self):
        return round(2 * math.pi * self.radius, 5)
    
    def calc_square(self):
        return round(math.pi * self.radius ** 2, 5)
    
    def paint(self):
        theta = np.linspace( 0 , 2 * np.pi , 150 )

        a = self.radius * np.cos( theta ) + self.coord[0]
        b = self.radius * np.sin( theta ) + self.coord[1]
        figure, axes = plt.subplots( 1 )
        
        axes.plot( a, b )
        axes.set_aspect( 1 )
        
        plt.show()


class Option:
    def __init__(self, name, coords, *args):
        self.name = name
        if self.name == 'Triangle perimeter':
            self.descr = self.get_triangle_perimeter(coords)
        elif self.name == 'Rectangle perimeter':
            self.descr = self.get_rectangle_perimeter(coords)
        elif self.name == 'Circle perimeter':
            self.descr = self.get_circle_perimeter(coords, *args)
        elif self.name == 'Triangle square':
            self.descr = self.get_triangle_square(coords)
        elif self.name == 'Rectangle square':
            self.descr = self.get_rectangle_square(coords)
        elif self.name == 'Circle square':
            self.descr = self.get_circle_square(coords, *args)

    def __str__(self):
        return f'{self.descr}'

    @staticmethod
    def get_triangle_perimeter(coords):
        return Triangle(coords).calc_perimeter()
    
    @staticmethod
    def get_rectangle_perimeter(coords):
        return Rectangle(coords).calc_perimeter()
    
    @staticmethod
    def get_circle_perimeter(coords, radius):
        return Circle(coords, radius).calc_perimeter()
    
    @staticmethod
    def get_triangle_square(coords):
        return Triangle(coords).calc_square()
    
    @staticmethod
    def get_rectangle_square(coords):
        return Rectangle(coords).calc_square()
    
    @staticmethod
    def get_circle_square(coords, radius):
        return Circle(coords, radius).calc_square()


print(Option('Triangle perimeter', [(41, 6), (5, 5), (2, 32)]))
print(Option('Triangle square', [(41, 6), (5, 5), (2, 32)]))

print(Option('Rectangle perimeter', [(2, 2), (4, 2), (4, 1), (2, 1)]))
print(Option('Rectangle square', [(2, 2), (4, 2), (4, 1), (2, 1)]))

print(Option('Circle perimeter', (1, 0), 2))
print(Option('Circle square', (1, 0), 2))
