from abc import ABC


class Shape(ABC):

    def __str__(self):
        return ''
    

class Circle(Shape):

    def __init__(self, radius) -> None:
        self.radius = radius

    def resize(self, factor):
        self.factor *= factor
    
    def __str__(self):
        return f'A circle with radius {self.radius}'


class Square(Shape):

    def __init__(self, side) -> None:
        self.side = side

    def resize(self, factor):
        self.factor *= factor
    
    def __str__(self):
        return f'A square with side {self.side}'


class ColouredShape(Shape):

    def __init__(self, shape, colour) -> None:
        self.colour = colour
        self.shape = shape
    
    def __str__(self):
        return f'{self.shape} has colour {self.colour}'


class TransparantShape(Shape):
    def __init__(self, shape, trans) -> None:
        self.shape = shape
        self.trans = trans

    def __str__(self):
        return f'{self.shape} has a transparancy of {self.trans}%'

circle = Circle(2)
print(circle)

red_circle = ColouredShape(circle, 'red')
print(circle)
print(red_circle)

red_dim_circle = TransparantShape(red_circle, 0.5)
print(red_dim_circle)