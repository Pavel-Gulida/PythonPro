import math

#1
class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Triangle(Shape):
    def __init__(self, x, y, side_a, side_b, side_c):
        super().__init__(x, y)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def square(self):
        half_per=(self.side_a + self.side_b + self.side_c)/2
        return math.sqrt(half_per*(half_per-self.side_a)*
                         (half_per-self.side_b)*(half_per-self.side_c)).__round__(2)


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2



class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def square(self):
        return self.width * self.height * math.sin(self.angle).__round__(2)


    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures).__round__(2)

    def __str__(self):
        pass


r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

par = Parallelogram(1, 2, 20, 30, 45)
print(par.square())

t = Triangle(0,0, 3, 4, 5)
print(t.square())

scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)

print(scene.total_square())

#2
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

def contains(self, p: Point):
    if p.x ** 2 + p.y ** 2 <= self.radius ** 2:
        return True
    return False

Circle.__contains__=contains
print(Point(1, 2) in Circle(1, 2, 10))
