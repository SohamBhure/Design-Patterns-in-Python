class Circle:
  def __init__(self, radius):
    self.radius = radius
    self.p = 'Circle'

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    temp_str = 'A circle of radius '+ str(self.radius)
    return temp_str

class Square:
  def __init__(self, side):
    self.side = side
    self.p = 'Square'

  def __str__(self):
    temp_str = 'A square with side '+ str(self.side)
    return temp_str
    


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    if self.shape.p == 'Circle':
        self.shape.resize(factor)

  def __str__(self):
    temp_str = str(self.shape)+ ' has the color ' + str(self.color)
    return temp_str