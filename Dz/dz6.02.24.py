import math
import time
from math import pi
pause = 1
time.sleep(pause)

print("Расчет площади фигур =>")
time.sleep(pause)

print("Выберите фигуру\n1 - треугольник\n2 - прямоугольник\n3 - круг ")
time.sleep(pause)

figure = int(input("Сделайте свой выбор: "))
s = None
if figure == 1:
    a = int(input("Введите сторону a: "))
    b = int(input("Введите сторону b: "))
    c = int(input("Введите сторону c: "))
    p = (a+b+c)/2
    s = p*(p-a)*(p-b)*(p-c)
    s = math.sqrt(s)
    print("Площадь треугольника равна:", round(s, 2))
elif figure == 2:
    a = int(input("Введите сторону a: "))
    b = int(input("Введите сторону b: "))
    s = a*b
    print("Площадь прямоугольника равна:", round(s, 2))
elif figure == 3:
    a = int(input("Введите радиус треугольника: "))
    s = pi * (a ** 2)
    print()
    print("Площадь круга равна:", round(s, 2))
else:
    print("Вы ввели неправильное значение!")