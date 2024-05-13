import matplotlib.pyplot as plt
import pylab
class figure:
    def __init__(self, P, S, **dots):
        self.P = P
        self.S = S
        self.__dict__.update(dots)
class triangle(figure):
    def __init__(self, **dots):
        super().__init__(self.p(dots['dot1'], dots['dot2'], dots['dot3']), 
                         self.s(dots['dot1'], dots['dot2'], dots['dot3']), 
                         dot1 = dots['dot1'], dot2 = dots['dot2'], dot3 = dots['dot3'])
        
    def side(self, dot1, dot2, dot3):
        l1 = ((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)**0.5
        l2 = ((dot2[0]-dot3[0])**2+(dot2[1]-dot3[1])**2)**0.5
        l3 = ((dot3[0]-dot1[0])**2+(dot3[1]-dot1[1])**2)**0.5
        return l1, l2, l3
    
    def p(self, dot1, dot2, dot3):
        l1, l2, l3 = self.side(dot1, dot2, dot3)
        P = l1 + l2 + l3
        return P
    
    def s(self, dot1, dot2, dot3):
        S = 0.5 * abs((dot2[0] - dot1[0] ) * (dot3[1] - dot1[1]) 
                      - (dot3[0] - dot1[0] ) * (dot2[1] - dot1[1]))
        return S
    
    def paint(self):
        plt.xlim(-2, 8)
        plt.ylim(-2, 8)
        plt.grid()
        axes = plt.gca()  
        axes.set_aspect("equal")
        axes.add_patch(plt.Polygon([[self.dot1[0], self.dot1[1]],
                                    [self.dot2[0], self.dot2[1]],
                                    [self.dot3[0], self.dot3[1]]],
                                   fill = True,
                                   closed = True,
                                   color= 'blue'))
        plt.show()
TRNGL = triangle(dot1 = [4, 8], dot2 = [3, 1], dot3 = [7, 6])
print('Стороны треугольника:', TRNGL.side(TRNGL.dot1, TRNGL.dot2, TRNGL.dot3))
print('Периметр:', TRNGL.P)
print('Площадь:', TRNGL.S)
TRNGL.paint()






class rectangle(figure):
    def __init__(self, **dots):
        super().__init__(self.p(dots['dot1'], dots['dot2'], dots['dot3']), 
                         self.s(dots['dot1'], dots['dot2'], dots['dot3']), 
                         dot1 = dots['dot1'], 
                         dot2 = dots['dot2'], 
                         dot3 = dots['dot3'], 
                         dot4 = dots['dot4'])
        
    def side(self, dot1, dot2, dot3):
        l1 = ((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)**0.5
        l2 = ((dot3[0]-dot1[0])**2+(dot3[1]-dot1[1])**2)**0.5
        return l1, l2
    
    def p(self, dot1, dot2, dot3):
        l1, l2 = self.side(dot1, dot2, dot3)
        P = 2*(l1 + l2)
        return P
    
    def s(self, dot1, dot2, dot3):
        l1, l2 = self.side(dot1, dot2, dot3)
        S = l1*l2
        return S
    
    def paint(self):
        plt.xlim(-2, 8)
        plt.ylim(-2, 8)
        plt.grid()
        axes = plt.gca()
        axes.set_aspect("equal")
        axes.add_patch(plt.Polygon([[self.dot1[0], self.dot1[1]],
                                    [self.dot2[0], self.dot2[1]],
                                    [self.dot4[0], self.dot4[1]],
                                    [self.dot3[0], self.dot3[1]]],
                                   fill = True,
                                   closed = True,
                                   color= 'blue'))
        
        plt.show()
RECT = rectangle(dot1 = [4, 1], dot2 = [1, 0], dot3 = [8, 0], dot4 = [5, 3])
print('Стороны прямоугольника:', RECT.side(RECT.dot1, RECT.dot2, RECT.dot3))
print('Периметр:', RECT.P)
print('Площадь:', RECT.S)
RECT.paint()







class circle(figure):
    def __init__(self, **dots):
        super().__init__(self.p(dots['dot1'], dots['dot2']), 
                         self.s(dots['dot1'], dots['dot2']),
                         dot1 = dots['dot1'], 
                         dot2 = dots['dot2'])
        
    def r(self, dot1, dot2):
        rr = ((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)**0.5
        return rr
    
    def p(self, dot1, dot2):
        rr = self.r(dot1, dot2)
        print(rr)
        P = 3.14 * rr * 2
        return P
    
    def s(self, dot1, dot2):
        rr = self.r(dot1, dot2)
        S = rr**2 * 3.14
        return S
    
    def paint(self):
        plt.xlim(-8, 8)
        plt.ylim(-8, 8)
        plt.grid()
        axes = plt.gca()
        axes.set_aspect("equal")
        axes.add_patch(plt.Circle((0, 0),
                       radius= self.r(self.dot1, self.dot2),
                       color= 'blue'))
        plt.show()
CRCL = circle(dot1 = [0, 0], dot2 = [0, 5])
print(CRCL.r(CRCL.dot1, CRCL.dot2))
print(CRCL.P)
print(CRCL.S)
CRCL.paint()






