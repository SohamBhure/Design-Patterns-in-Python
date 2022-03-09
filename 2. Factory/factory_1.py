from cmath import cos, sin
from enum import Enum
from re import X


class CoordinateSystem(Enum):

    CART = 1
    POLAR = 2

class Point:

    '''
    def __init__(self, a, b, system=CoordinateSystem.CART) -> None:
        
        if system == 1:
            self.x = a
            self.y = b

        if system == 2:
            self.x = a * cos(b)
            self.y = a * sin(b)
    '''

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f'x: {self.x}\ny: {self.y}'

    @staticmethod
    def new_car_point(x,y):
        return Point(x,y)

    @staticmethod
    def new_polar_point(rho,theta):
        return Point(rho * cos(theta), rho * sin(theta))


p = Point(2,3)
print(p)

p1 = Point.new_car_point(2,3)
p2 = Point.new_polar_point(2,3)
print(p1)
print(p2)
