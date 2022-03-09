from abc import ABC


class Renderer(ABC):

    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):

    def render_circle(self, radius):
        print("Drawing a circle of radius: " + str(radius))


class RasterRenderer(Renderer):

    def render_circle(self, radius):
        print("Drawing pixels for a circle of radius: " + str(radius))    


class Shape:

    def __init__(self, renderer):
        self.renderer = renderer
    
    def draw(self):
        self.renderer.render_circle(self.radius)
        

    def resize(self, factor):
        self.radius *= factor 
        pass


class Circle(Shape):

    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius


raster = RasterRenderer()
vector = VectorRenderer()

circle = Circle(vector, 5)
circle.draw()
circle.resize(10)
circle.draw()