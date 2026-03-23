import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        if radius < 0: 
            raise ValueError("радіус не може бути менший за нуль")
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def calculate_area(self) -> float:
        return self.length * self.width
    
class Triangle(Shape):
    def __init__(self, height: float, side: float):
        self.height = height
        self.side = side

    def calculate_area(self) -> float:
        return self.height * self.side / 2
    
def print_areas(shapes):
    for shape in shapes:
        print(f"Площа {shape.__class__.__name__}: {shape.calculate_area():.2f}")
    
shapes_list = [
    Circle(5),
    Rectangle(10, 5),
    Triangle(4, 6)
]
print_areas(shapes_list)