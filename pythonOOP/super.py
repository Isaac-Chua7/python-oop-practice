

class Shape():
    def __init__(self, colour, is_regular):
        self.colour = colour
        self.is_regular = is_regular

    def describe(self):
        print(f"I am {self.colour} and I am {"a regular polygon" if self.is_regular else "an irregular polygon"}")
    
class Square(Shape):
    def __init__(self, colour, is_regular, width):
        super().__init__(colour, is_regular)
        self.width = width

    def describe(self):
        super().describe()
        print(f"I also have an area of {self.width*self.width} cm²")


class Trapezium(Shape):
    def __init__(self, colour, is_regular, height, top_length, bottom_length):
        super().__init__(colour, is_regular)
        self.height = height
        self.top_length = top_length
        self.bottom_length = bottom_length
    
    def describe(self):
        super().describe()
        print(f"I also have an area of {(self.top_length+self.bottom_length)/2*self.height} cm²")

square = Square("red", True, 6.7)
square.describe()

trap = Trapezium("blue", True, height=10, top_length=12, bottom_length=3)
trap.describe()