
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area1 = self.width * self.height

    @staticmethod
    def area(width, height):
        return width * height

    @classmethod
    def hello(cls):
        print "hello fabric"

r = Rectangle(2, 5)
print r.area(2, 5)
r.hello()