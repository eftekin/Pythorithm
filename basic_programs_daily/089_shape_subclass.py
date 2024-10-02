# Define a class named Shape and its subclass Square. The Square class has an init
# function which takes a length as argument. Both classes have an area function which
# can print the area of the shape where Shape's area is 0 by default.


class Shape:
    def __init__(self) -> None:
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length) -> None:
        super().__init__()
        self.length = length

    def area(self):
        return self.length**2


shape = Shape()
square = Square(float(input("Enter the shape of the square: ")))

print("Shape's are by default:", shape.area())
print("Area of the square:", square.area())
