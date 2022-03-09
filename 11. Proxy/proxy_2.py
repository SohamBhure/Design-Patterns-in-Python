class Bitmap:
    
    def __init__(self, filename):
        self.filename = filename
        print("Loading image from file")

    def draw(self):
        print("Drawing Image")


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")


class LazyBitmap:

    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    
    def draw(self):    
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)

        self._bitmap.draw()    


bmp = LazyBitmap('faces.jpg')
draw_image(bmp)

