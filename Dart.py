
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Printable:
    def print_info(self):
        pass

class Rectangle(Shape, Printable):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def print_info(self):
        print(f"Color: {self.color}, Width: {self.width}, Height: {self.height}")

class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)

    def area(self):
        return self.width ** 2

class DataReader:
    @staticmethod
    def read_data(filename):
        with open(filename, 'data.txt') as file:
            data = file.readlines()
        return data

def print_data_from_file(filename):
    data = DataReader.read_data(filename)
    for line in data:
        print(line.strip())

circle = Circle("Red", 5)
print("Circle Area:", circle.area())

rectangle = Rectangle("Blue", 4, 6)
rectangle.print_info()

square = Square("Green", 5)
print("Square Area:", square.area())

print_data_from_file("data.txt")

