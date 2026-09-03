#Create a hierarchical inheritence structure where a parent class shape
#inherited by circle, rectangle, and triangle each having a seperate area calculation method
import math
class Shape:
    def __init__(self,shape_name):
       self.shape_name=shape_name
       print(f"Area of {self.shape_name}")
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius,shape_name):
        self.radius=radius
        super().__init__(shape_name)
    def area(self):
        print(f"Area of circle with radius {self.radius}: {math.pi*self.radius**2}")
class Rectangle(Shape):
    def __init__(self,length,width,shape_name):
        self.length=length
        self.width=width
        super().__init__(shape_name)
    def area(self):
        print(f"Area of Rectangle with length {self.length}, and width {self.width}: {self.length*self.width}")
class Triangle(Shape):
    def __init__(self,base,height,shape_name):
        self.base=base
        self.height=height
        super().__init__(shape_name)
    def area(self):
        print(f"Area of triangle with base {self.base}: and height {self.height}: {(0.5*self.base*self.height)} ")
cobj=Circle(5,"Circle")
cobj.area()
robj=Rectangle(5,3,"Rectangle")
robj.area()
tobj=Triangle(5,6,"Triangle")
tobj.area()
        