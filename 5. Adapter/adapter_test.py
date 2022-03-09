from unittest import TestCase

class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return (rc.square.width) * (rc.square.height)

class SquareToRectangleAdapter:
    def __init__(self, square):
        # TODO
        self.square = square
        #self.height = square.side
        #self.width = square.side
    
    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side

class Evaluate(TestCase):
    def test_exercise(self):
        sq = Square(11)
        adapter = SquareToRectangleAdapter(sq)
        self.assertEqual(121, calculate_area(adapter))
        sq.side = 10
        self.assertEqual(100, calculate_area(adapter))

sq = Square(11)
adapter = SquareToRectangleAdapter(sq)
print(calculate_area(adapter))

sq.side = 10
print(calculate_area(adapter))

