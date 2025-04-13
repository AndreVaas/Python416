import math


class Square:
    __count = 0

    @staticmethod
    def square_triangle_geron(a, b, c):
        p = (a + b + c) // 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        Square.__count += 1
        return s

    @staticmethod
    def square_triangle(a, h):
        s = (a * h) // 2
        Square.__count += 1
        return s

    @staticmethod
    def square_square(a):
        s = a ** 2
        Square.__count += 1
        return s

    @staticmethod
    def square_rectangle(a, b):
        s = a * b
        Square.__count += 1
        return s

    @staticmethod
    def get_count():
        return Square.__count


print("Площадь треугольника по формуле Герона:", Square.square_triangle_geron(3, 4, 5))
print("Площадь треугольника через основание и высоту:", Square.square_triangle(6, 7))
print("Площадь квадрата:", Square.square_square(7))
print("Площадь прямоугольника:", Square.square_rectangle(2, 6))
print("Количество подсчетов площади:", Square.get_count())
