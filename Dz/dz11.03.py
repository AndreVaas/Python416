from math import pi

area = {'Circle': lambda a: (a ** 2) * pi, 'Rectangle': lambda a, b: a * b,
        'Trapezoid': lambda a, b, h: (a + b) / 2 * h}


print("Площадь окружности радиуса 2: ", area['Circle'](2))
print("Площадь прямоугольника размером 10Х13: ", area['Rectangle'](10, 13))
print("Площадь трапеции для a=7, b=5, h=3: ", area['Trapezoid'](7, 5, 3))