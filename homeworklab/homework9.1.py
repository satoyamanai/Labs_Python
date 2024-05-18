import matplotlib.pyplot as plt
import numpy as np

class GeometricFigures:
    def __init__(self, perimeter, area, coordinates):
        self.perimeter = perimeter
        self.area = area
        self.coordinates = coordinates

    def paint(self):
        pass

class Triangle(GeometricFigures):
    def __init__(self, side1, side2, side3, coordinates):
        perimeter = side1 + side2 + side3
        s = perimeter / 2
        area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
        super().__init__(perimeter, area, coordinates)

    def paint(self):
        plt.figure()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.plot([self.coordinates[0], self.coordinates[0] + 3, self.coordinates[0] + 1.5, self.coordinates[0]],
                 [self.coordinates[1], self.coordinates[1], self.coordinates[1] + 2.598, self.coordinates[1]], 'b-')
        plt.title('Triangle')
        plt.show()

class Rectangle(GeometricFigures):
    def __init__(self, length, width, coordinates):
        perimeter = 2 * (length + width)
        area = length * width
        super().__init__(perimeter, area, coordinates)

    def paint(self):
        plt.figure()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.Rectangle(self.coordinates, 3, 5, fill=None)
        plt.title('Rectangle')
        plt.show()

class Circle(GeometricFigures):
    def __init__(self, radius, coordinates):
        perimeter = 2 * np.pi * radius
        area = np.pi * (radius ** 2)
        super().__init__(perimeter, area, coordinates)

    def paint(self):
        circle = plt.Circle(self.coordinates, 3, fill=None)
        plt.figure()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.gca().add_artist(circle)
        plt.title('Circle')
        plt.show()

# 示例:
triangle = Triangle(3, 4, 5, (0, 0))
rectangle = Rectangle(3, 5, (0, 0))
circle = Circle(3, (0, 0))

print("Triangle - Perimeter:", triangle.perimeter, "Area:", triangle.area)
triangle.paint()

print("Rectangle - Perimeter:", rectangle.perimeter, "Area:", rectangle.area)
rectangle.paint()

print("Circle - Perimeter:", circle.perimeter, "Area:", circle.area)
circle.paint()