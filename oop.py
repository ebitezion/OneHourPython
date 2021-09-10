class Shape:
    """
    Shape(length(optional),breadth(optional))
    """
    radius=8.0
    def __init__(self,length=0,breadth=0):
        self.length=length
        self.breadth=breadth
         
    def show(self,val):
        print(str(val))

class Rect(Shape):
    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    @classmethod
    def area(cls):
        return 3.142* cls.radius* cls.radius
    @staticmethod
    def perimeter():
        pass


shp=Rect(2,4)
shp.show(shp.area())
shp.show(Circle.area())
