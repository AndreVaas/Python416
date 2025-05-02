from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def print_pic(self):
        pass


class Rectangle(Shape):
    def __init__(self, color, w, h):
        super().__init__(color)
        self.w = w
        self.h = h

    def print_pic(self):
        for i in range(self.h):
            print(["*" + "*" * (self.w - 2) + "*", "*" * self.w][i % (self.h - 1) == 0])

    def perimeter(self):
        return 2 * (self.w + self.h)

    def area(self):
        return self.w * self.h

    def print_info(self):
        print(f"\n===Прямоугольник===\nДлинна: {self.h}\nШирина: {self.w}\n"
              f"Цвет: {self.color}\nПлощадь:{self.area()}\n"
              f"Периметр:{self.perimeter()}")
        self.print_pic()


class Square(Shape):
    def __init__(self, color, a):
        super().__init__(color)
        self.a = a

    def perimeter(self):
        return 4 * self.a

    def area(self):
        return self.a ** 2

    def print_info(self):
        print(f"\n===Квадрат===\nСторона: {self.a}\n"
              f"Цвет: {self.color}\nПлощадь:{self.area()}\n"
              f"Периметр:{self.perimeter()}")
        self.print_pic()

    def print_pic(self):
        for i in range(self.a):
            print(["*" + "*" * (self.a - 2) + "*", "*" * self.a][i % (self.a - 1) == 0])


class Triangle(Shape):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def print_info(self):
        print(f"\n===Треугольник===\nСторона 1: {self.a}\nСторона 2: {self.b}\n"
              f"Сторона 3: {self.c}\n"
              f"Цвет: {self.color}\nПлощадь:{self.area():.2f}\n"
              f"Периметр:{self.perimeter()}")
        self.print_pic()

    def print_pic(self):
        for i in range(self.c):
            print(" " * (self.c - 1 - i) + "*" * (1 + i * 2))


t = Triangle("yellow", 11, 6, 6)
r = Rectangle("red", 7, 3)
s = Square("green", 3)
shape = [s, r, t]
for g in shape:
    g.print_info()
