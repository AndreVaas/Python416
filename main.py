# name = "admin" # переменная
import locale
import math
import time
from http.cookiejar import join_header_words
from itertools import count
from logging import setLogRecordFactory
from math import trunc
from operator import index
from queue import PriorityQueue

# print("Hello, " + name + "!")
# age = 20
# print(name + str(age))
# print(age)
# age = 15.2
# print(age)
# print(type(name))
# print(type(age))

# a = 4
# b = 5
# print(id(a))
# print(id(b))
# a = b # 5
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)

# _first_name = "admin"
# print(_first_name)
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# name = "Никита"
# age = 25
# print("Меня " + "зовут " + name + ". Мне " + str(age) + " лет.")


# a = 1
# b = 2
# print("a:",a)
# print("b:",b)
# Первый способ
# c = a
# a = b
# b = c
# Второй способ
# a, b = b, a
# Третий способ
# a= a + b # 1 + 2 = 3
# b = a - b # 3 - 2 = 1
# a = a - b # 3 - 1 = 2
# print("a:",a)
# print("b:",b)

# print("Строка \
# символов")
# print('Строка \nсимволов')
# print("\tДокумент \"file.txt\" находиться по пути : D\\folder\\file.txt ")


# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3 * 3)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)
# print(7 // 2) # Целочисленное деление
# print(7 ** 2) # Возведение в степень
# print(7 % 2) # Остаток от деления

# a = 5
# b = 7
# c = 3
# print("Сумма:",a+b+c)
# print("Произведение:",a*b*c)
# print("Среднее арифметическое:",(a+b+c)/3)

# print(6 + 4 * 5 ** 2 + 7) # 113
# print((6 + 4) * (5 ** 2 + 7)) # 320

# num = 10
# num +=5 # Num(10) + 5 = 15
# print(num)
#
# num -=3 # Num(15) - 3 = 12
# print(num)
#
# num *=4 # num(12) * 4 = 48
# print(num)
#
# num **=2 # Num(48) ** 2 = 2304
# print(num)

# Первый способ перевернуть в обратную сторону числовой ряд
# num = 4321  # 4321
# print(num)
#
# a = num % 10
# print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# # print(num)
# d = num % 10
# numinvert =  a * 1000 + b * 100 + c * 10 + d
# print("d:", d)
# print("Обратное число:", numinvert )


# Второй способ перевернуть в обратную сторону числовой ряд
# num = 4321 # 4321
# print("Исходное число:", num)
#
# res = num % 10 * 1000  # 1000
# num //= 10  # 432
# res += num % 10 * 100  # 200
# num //= 10  # 43
# res += num % 10 * 10  # 30
# num //= 10  # 4
# res += num % 10
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
# # res = int(num1) + num2
# print(res)  #

# print(int(3.8))
# print(round(3.8))
# print(type(round(3.8)))
# print(type(round(3.891, 2)))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)

# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end=" ")
# print("Новая строка")

# name = input("Введите имя: ")
# print("Ваше имя:", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res  )


# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# num4 = int(input("Введите четвертое число: "))
# sum1 = num1 + num2
# sum2 = num3 + num4
# delenie = sum1 / sum2
# print("Результат = ", round(delenie,2)  )

# b1 = True
# b2 = False
# print(type(b1))
# print(b1 + 5) # 1 + 5
# print(b2 + 5)

# print(bool("python")) #True
# print(bool("")) # False
# print(bool(5))#True
# print(bool(0)) # False
# print(bool(0.1))#True
# print(bool(0.0)) # False
# print(bool(False)) # False
# print(bool(None)) # False

# a = None
# print(a)
# print(type(a))
# print(7 == 7) # True
# print(2 + 5 == 7/3) # False
# print(2 + 5 != 7 / 3)
# print(8 > 5)
# print(8 > 8)
# print(8 >= 8)
# print(9 > 9)
# print(9 >= 9)
# print("python" > "Python") # 112 > 80 => Сравнивает код символа первой буквы

# print(2 < 4 < 9)  # True && True => True
#
# print(2 * 5 > 7 >= 4 + 3)  # 10 > 7 >=7 True && True => True
# print(3 * 3 <= 7 >= 2)  # 9 <= 7 >=2 False && True => False

# a = "10"
# b = 5
# c = a == b
# print(a, b, c)


# num = int(input("Введите пятизначное число: "))
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = num // 10
# e = num % 10
#
# product_of_numbers = a * b * c * d * e
# arithmetic_mean = (a + b + c + d + e) / 5
# print("Произведение чисел:", product_of_numbers)
# print("Среднее арифметическое:", arithmetic_mean)

# print(5 - 3 == 2 and 1 + 3 == 4)  # true == true => true
# print(5 - 3 == 2 and 1 + 3 < 4)  # true == false => false
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # true or true => true
# print(5 - 3 == 2 or 1 + 3 < 4)  # true or false => true !
#
# print(not 9 - 5)  # not = ! Обращает true в false
# print(not 7 - 7)
# a = 2
# print("a:", a)


# cnt = 15
# if cnt < 10:
#     cnt += 1
#       print(cnt)
#
# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = 25
# b = 25
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a == b")
# else:
#     print("b > a")

# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# c = input("Введите третье число: ")
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")
###
# a = int(input("Введите день недели: "))
# if 1 <= a <= 5:  # (a >= 1) and (a <= 5)
#     print("Рабочий день", end="")
#     if a == 1:
#         print(" - понедельник")
#     if a == 2:
#         print(" - вторник")
#     if a == 3:
#         print(" - среда")
#     if a == 4:
#         print(" - четверг")
#     if a == 5:
#         print(" - пятница")
#
# elif a == 6 or a == 7:
#     print("Выходной день", end="")
#     if a == 6:
#         print(" - суббота")
#     if a == 7:
#         print(" - воскресенье")
# else:
#     print("Такого дня недели нет")
####

# a = int(input("Введите номер месяца: "))
# if a == 12 or a == 1 or a == 2:  # (a >= 1) and (a <= 5)
#     print("Зима")
# elif a == 3 or a == 4 or a == 5:
#     print("Весна")
# elif a == 6 or a == 7 or a == 8:
#     print("Лето")
# elif a == 9 or a == 10 or a == 11:
#     print("Осень")
# else:
#     print("Некорректное значение")
####
# season = int(input("Введите номер месяца: "))
# if 1 <= season <= 12:
#     print("Время года: ", end="")
# if 1 <= season <= 2 or season == 12:
#     print("Зима")
# if 3 <= season <= 5:
#     print("Весна")
# if 6 <= season <= 8:
#     print("Лето")
# if 9 <= season <= 11:
#     print("Осень")
#     else:
#     print("Такого месяца нет")
#######
# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
#
# else:
#     print("Ошибка ввода!")
#####
# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ворон", end="")
#     if n == 1:
#         print("а", n)
#     if 2 <= n <= 4:
#         print("ы", n)
#     if 5 <= n <= 9 or n == 0:
#         print("", n)
#
# else:
#     print("Ошибка ввода")
####

# password = "user"
# match password:
#   case "admin":
#     print("Администратор")
#   case "user":
#     print("Пользователь")
#   case _:
#     print("Пароль неверен")


# day = 'понедельник'
# time = 9
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# a, b = 10, 20
# print( a if a < b else b)

# a, b = 30, 20
# print("На 0 делить нельзя" if b == 0 else a / b)

# n = int(input("Введите сколько у вас копеек (от 0 до 99): "))
# if 0 <= n <= 99:
#     if 11 <= n <= 14:
#         print("У вас", n, "копеек")
#     else:
#         m = n % 10
#         if m == 1:
#             print("У вас", n, "копейка")
#         elif 2 <= m <= 4:
#             print("У вас", n, "копейки")
#         else:
#             print("У вас", n, "копеек")
# else:
#     print("Ошибка ввода!")
####

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на ноль")
# else: # Когда в блоке try не возникло исключений
#     print("Все нормально. Вы ввели", n, "и", m)
# finally: # Выполниться в любом случае
#     print("Конец программы")


# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     print(int(m) + int(n))
# except ValueError:
#     print(str(m) + str(n))
# finally:
#     print(m + n)

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(m + n)

#
# while условие:
#     блок_кода

# Итерация - оди шаг цикла

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
#
# print()
#
# j = 2
#
# while j <= 20:
#     print(j, end=" ")
#     j += 2


# n = int(input("Укажите количество звездочек: "))
# i = 0
# while i <= n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество звездочек: "))
# # print("*" * n)
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a)
#         res += a
#     a += 1
# print(res)

# n = input("Введите целое число:")
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число:")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\n Цикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# res = 1
# while True:
#     n = int(input("Введите положительное или отрицательное число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)
# print("\nЦикл завершен")


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 0
# while i < 10:
#     print(i)
#     i += 1
# print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# n = int(input("Укажите количество символов: "))
# m = input("Укажите тип символа: ")
# r = int(input("Укажите ориентацию линии (0 - горизонтальная, 1 - вертикальная: "))
# # print("*" * n)
# if r == 0:
#     while n > 0:
#         print(m, end=" ")
#         n -= 1
# elif r == 1:
#     while n > 0:
#         print(m)
#         n -= 1
# print("\nПрограмма завершена")

# count = input("Укажите кол-во символов: ")
# while type(count) is not int:
#     try:
#         count = int(count)
#     except ValueError:
#         print("Введите целое число")
#         count = input("Введите целое число: ")
#         types = input("Укажите Вид символа: ")
#         orient = input("Укажите направление, 0 - по вертикале, 1 -по горизонтали: ")
#         i = 0
#         while i <= count:
#             if orient == 1:
#                 print(types, end=" ")
#                 if orient == 0:
#                     print(types, end="\n")
#                     i += 1
#                     while type(orient) is not int:
#                         i = 0
#                     try:
#                         orient = int(orient)
#                     if orient == 0 or orient == 1:
#                         pass
#                         else:
#                             print("Неверное направление!")
#                             orient = input("Введите направление 1 или 0: ")
#                     except ValueError:
#                             print("Неверное направление!")
#                             orient = input("Введите направление 1 или 0: ")
#                             i += 1


# for i in "Hello":
#     print(i)
#
# for i in "Hello", "World":
#     print(i)


# range(start=0,stop,step=1)
# for i in range(0,10,1): # i = 0, i < 10; i+=1
#     print(i, end=" ")
#
# print()
# j = 10
# while j > 0:
#     print(j, end=" ")
#     j -= 2
#

# a = int(input("Введите целое число: "))
# for i in range(1, a):
#     if  a % i == 0:
#         print(i, end=" ")


# for i in range(11, 100, 11):
#     print(i, end=" ")
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Конец цикла")


# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# string = [letter * 2 for letter in "Python"]
# print(string)
#
# for letter in "Python":
#     print(letter * 2, end="\t")


# Список ( list)

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(type(nums))
#
# num1 = list()
# print(num1)
# print(type(num1))

# nums = [8, 3, 9, 4, 1, "one", True]
# print(nums)
# print(nums[0])
# print(nums[-5])
# print(nums[-1])
# print(nums[4])
# print(nums[5])
# print(nums[6])

# nums = [8, 3, 9, 4, 1]
# print(nums)
# nums[1] = 256
# print(nums[1])
# nums[3] += 100
# print(nums)

# nums = [8, 3, 9, 4, 1]
# print(nums, id(nums))
# print(nums[0], id(nums[0]))
# print(nums[1], id(nums[1]))
# nums[1] = 256
# print(nums[1], id(nums[1]))
# print(nums, id(nums))

# nums = [8, 3, 9, 4, 1]
# nums2 = [11, 12, 13]
# n = nums + nums2
# print(n)
# print(n * 2)

# print(list("Hello"))

# print(range(10))
# print(list(range(10)))
# print(list(range(2,10)))
# print(list(range(10,2,-2)))

# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)

# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

#
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# minusSum = 0
# for num in a:
#     if num < 0:
#         minusSum += num
# print("Сумма отрицательных элементов:", + minusSum)

### Вариант 2
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# minusSum = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         minusSum += a[i]
# print("Сумма отрицательных элементов:", + minusSum)
#################################################################################################################
# a = list(range(10,100,10))
# print(a)
#
# for i in range(len(a)):
#     print(a[i] + 2, end=" ")
# print()
#
# for i in a:
#     print(i + 2, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#  for i in range(len(a)):
#      if a[i] % 2 == 0:
#          print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in a:
#     if i > i - 1:
#         print(i, end=" ")

#################################################################################################################

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество четных элементов:", k)
# print("Сумма нечетных элементов:", s)

######### Вариант 2###############################################################################################

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("Количество четных элементов:", k)
# print("Сумма нечетных элементов:", s)

##################################################################################################################

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         k += 1
#         s += a[i]
# print("Среднее арифметическое:", s / k)

##################################################################################################################


# Срез
# Список[start:stop:step]

# s = [9, 7, 2, 1, 17, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:3])
# print(s)
# print(s[::2])
# print(s[::-1]) # -1 разворачивает элементы списка
##################################################################################################################

# lst = list(range(1,8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1:])
# print(lst[::-7])
# print(lst[3:4:])
# print(lst[4:7:])
# print(lst[4:1:-1])
# print(lst[2:5:])
##################################################################################################################
# st = "Hello"
# print(st[1:3])
# print(st[::-1])
#
# st = "123456"
# print(st[1:3])
# num = st[::-1]
# print(num)
# print(type(num))
# num = int(num)
# print(num)
# print(type(num))
##################################################################################################################
# lst = list(range(1, 8))
# print(lst)lst[1:3] = [0, 0, 0, 0]
# print(lst)lst[1:2] = [20]
# lst[3] = [40, 50]
# print(lst)lst[15:16] = [100]
# print(lst)

##################################################################################################################

# Методы списков


# lst = list(range(1, 8))
# lst.append(99)  # Append добавляет элемент в конец списка
# print(lst)
# lst.extend([1, 2, 3])  # Extend добавляет список элементов в конец списка
# print(lst)
# lst.insert(1, 100) # insert  добавляет элемент в список в определеную позицию ( index_куда, object_что добавляем)
# print(lst)
# Добавляем в конец  списка ________________________________
# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)
# Добавляем в начало списка ________________________________
# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0, x)
# print(s)
##########
# a = [5, 9, 2, 1, 4, 3, 2]
# b = [4, 2, 1, 3, 7, 2]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
# Второй вариант
# a = [5, 9, 2, 1, 4, 3, 2]
# b = [4, 2, 1, 3, 7, 2]
# c = []
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
#
# print(c)
#
# # Третий вариант
# a = [5, 9, 2, 1, 4, 3, 2]
# b = [4, 2, 1, 3, 7, 2]
# c = []
# for element in a:
#     if element in b and element not in c:
#         c.append(element)
#
# print(c)


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
# for i in a:
#     num = 0
#     for n in a:
#         if i == n:
#             num += 1
#     if num == 1:
#         b.append(i)
#
# print(a)
# print()
# print(b)


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# num = a.count(6) # Метод Count показывает количество повторений элемента
# print(num)

# Решение через метод Count ####################

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         b.append(a[i])
# print(b)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
# print(a)
# for i in a:
#     if a.count(i) == 1:
#         print(i, end=" ")

# a = [1, 2, 3]
# b = [11, 22, 23, 4, 2]
# c = []
# if len(b) > len(a): # если длина списка b больше списка a
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else: # если длина списка a больше списка b
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# Второй вариант #########################
# Меняем переменные местами  a, b = b, a
# a = [1, 2, 3]
# b = [11, 22, 23, 4, 2]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
#
# print(c)


# lst = [11, 1, 22, 2, 33, 3, 55, 66, 22]
#
# # lst[5:] = []
# # del lst[2]
# lst.remove(22) # Метод Remove удаляет элемент из списка по значению(первое вхождение)
# print(lst)
# last = lst.pop() # удаляет последний элемент из списка и возвращает его
# print(last)
#
# last = lst.pop()
# second = lst.pop(-2)# удаляет элемент из списка и возвращает его, если индекса нет то получим исключения
# print(second)
# print(lst)
#
# lst.clear()# Clear удаляет все значения из списка
# print(lst)

# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# value = 33
# if value in lst:
#     ind = lst.index(value, 5, 9)# Возращает индекс первого вхождения искомого элемента, можно указать
#     #диапазон от какого до какого мы производим поиск, может выдавать исключение ValueError  если элемент не найден.
#     print(ind)
# print(lst)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# a = lst.copy()# Создает копию списка по другому адресу
# print(lst, id(lst))
# print(a, id(a))
#
# a.append(100)
# print(lst)
# print(a)
#
# lst[0] = 256
# print(lst, id(lst))
# print(a, id(a))

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
#
# # lst.reverse()# Разворачивает список в противоположную сторону
# # print(lst)
#
# lst. sort(reverse=True)
# print(lst)
# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s.sort(key=len, reverse=True)# Сортирует по длине если в key = len, по умолчанию по алфавиту, либо по возрастанию
# print(s)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# new_lst = sorted(lst, reverse=True)# Встроенная функция cоpдает новый сортированный список
# print(new_lst)
# print(lst)

# Генерация случайных данных


# print(random.random())
# print(random.randint(5, 10))
# print(random.randrange(5, 10, 2))
# print(random.uniform(10.5, 25.5))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
# print(random.choice(city_list))
# print(random.choice(s))
# print(random.choices(city_list, k=3))
# print(random.choices(s, k=3))
# random.shuffle(city_list)
# random.shuffle(s)
# print(city_list)
# print(s)

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# a = mas.copy()
# a.sort()
# n = a[0]
# print("Min:", n)
# value = n
# if value in a:
#     ind = mas.index(value, 0, 10)
#     print("Index min:", ind)
#     mas[:ind] = []
# print(mas)


#
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(len(mas))  # Длина списка
# print(min(mas))  # Минимальный элемент списка
# print(max(mas))  # Максимальный элемент списка
# print(sum(mas))  # Сумма элемент списка


# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max1 = max(mas)
# print("Максимальный элемент:", max1)
# mas.remove(max1)
# mas.insert(0, max1)
# print(mas)


# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(2 in mas)


# lst = []
# # if len(lst) == 0:
# #     print("Список пустой")
# print(bool(lst))
# if not lst:
#     print("Список пустой")  # Самая простая проверка пустой ли список
# else:
#     print("В списке есть элементы")
import random

# m = [
#     [1, 2, 3, 4],  # нулевой индекс
#     [5, 6, 7, 8],  # первый индекс
#     [9, 10, 11, 12]  # второй индекс
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# # print(m[2][1])
# # print(m[1][3])
#
# print("Вариант 1")
# print()
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
#
# print("Вариант 2")
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


# Модули

# import math
#
# print(math.sqrt(4)) # Корень из числа
# print(math.ceil(3.2)) # Округление в верхнюю сторону
# print(math.floor(3.2)) # округление в нижнюю сторону

# import math as m
# print(m.sqrt(4)) # Корень из числа
# print(m.ceil(3.2)) # Округление в верхнюю сторону
# print(m.floor(3.2)) # округление в нижнюю сторону

# from math import *
# print(sqrt(4)) # Корень из числа
# print(ceil(3.2)) # Округление в верхнюю сторону
# print(floor(3.2)) # округление в нижнюю сторону

# from math import sqrt, ceil, floor
# print(sqrt(4)) # Корень из числа
# print(ceil(3.2)) # Округление в верхнюю сторону
# print(floor(3.2)) # округление в нижнюю сторону

# import math
# print(dir(math))

# from math import pi
# print(pi)
# radius = int(input("Введите радиус окружности: "))
# print("Длинна окружности:", round(2 * pi * radius, 2))

# import time
# import locale

# print(time.time())
# print(time.ctime(32434234423))
# print(time.localtime())
# res = time.localtime()
# print(res.tm_year, "-", res.tm_mon, "-", res.tm_mday, sep="")
# print(time.strftime("Today is %B %d, %Y")) # % - Служебный символ в сочетании с B/b, D/d, Y/y в сочетании с функцией strftime
# print(time.strftime("%m/%d/%y, %H:%M:%S"))
#
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y %A "))
# start = time.monotonic()
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# result = time.monotonic()  - start
# print("Программа выполнена за", result, "секунд")
# import math
# import time
# from math import pi
# pause = 1
# time.sleep(pause)
#
# print("Расчет площади фигур =>")
# time.sleep(pause)
#
# print("Выберите фигуру\n1 - треугольник\n2 - прямоугольник\n3 - круг ")
# time.sleep(pause)
#
# figure = int(input("Сделайте свой выбор: "))
# s = None
# if figure == 1:
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     c = int(input("Введите сторону c: "))
#     p = (a+b+c)/2
#     s = p*(p-a)*(p-b)*(p-c)
#     s = math.sqrt(s)
#     print("Площадь треугольника равна:", round(s, 2))
# elif figure == 2:
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     s = a*b
#     print("Площадь прямоугольника равна:", round(s, 2))
# elif figure == 3:
#     a = int(input("Введите радиус треугольника: "))
#     s = pi * (a ** 2)
#     print()
#     print("Площадь круга равна:", round(s, 2))
# else:
#     print("Вы ввели неправильное значение!")

# Функции

# def hello(name, age):
#     print("Меня зовут " + str(name) + ". Мне " + str(age) + " лет.")
#
#
# hello("Irina", 28)
# hello("Ivan", 35)

# def get_sum(a, b):
#     print(a + b)
#
#
# y = 5
# x = 3
# get_sum(y, x)
# get_sum("addf", "fffh")

# def print_line(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# print_line(9, "+", "-")
# print_line(7, "x", "0")

# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# y = 5
# x = 7
# res = get_sum(x, y)
# print(res)

# def max_value(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(max_value(23,34))


# def get_ent(one, two):
#     if one > two:
#         return one + two
#     else:
#         return one - two
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# print(get_ent(a, b))

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([1, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))

# # Второй вариант
# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
# print(change([1, 2, 3]))
# print(change([1, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))

# def is_first_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(is_first_big(10,5))
# # print(is_first_big(5,10))
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if is_first_big(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_numb = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_numb = True
#     if len(password) >= 8 and has_upper:
#         return True
#     return False
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(2,c=5,3))
# print(get_sum(1,2,3,4))
# print(get_sum(1,2,3))
# print(get_sum(1,2))
# print(get_sum(1,2, d=2))

# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("ira",23)
# display_info(23,"Ira")
# display_info(age=23,name = "Ira")
# display_info("ira",23)

# def line_sim(count=20, symbol="-"):
#     print(count * symbol)
#
#
# line_sim(10, "+")
# line_sim(5, "*")
# line_sim(15, "#")
# line_sim(7)
# line_sim()

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1 == lst2)
# print(lst1 is lst2)
#
# a = "Hello"
# b = "Hello"
#
# print(a == b)
# print(a is b)

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)

# a = "Hello"
# print(a, id(a))
# a = a + "!"
# print(a, id(a))
#
# a = 3
# print(a, id(a))
# a = a + 5
# print(a, id(a))

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# print(lst(1))
# print(tpl[1])
# lst[1] = 50
# print(lst)
#
# tpl[1] = 50  # Кортеж не может изменятся!!
# print(tpl)

# a = 1, 2, 3, 4, 5 # Кортеж может быть и в таком виде
# print(a, type(a))

# a = tuple("Hello")
# print(a, type(a))

# a = (1, 2, 3, 4, 5) # Кортеж может быть и в таком виде
# print(a[2])
# print(a[1:3])
from random import randint
from zoneinfo import reset_tzpath

# print(tuple(i for i in range(10)))

# print(tuple(input("->") for i in range(5)))
# print(tuple(randint(50, 100) for i in range(10)))

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# # print(t3)
# # print(t3.count("l"))
# # if "e" in t3:
# #     print(t3.index("e" ))
# # else
# #     print("Такого элемента нет")
#
# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, a):
#     if a in tpl:
#         if tpl.count(a) == 1:
#             return tpl[tpl.index(a):]
#         else:
#             first = tpl.index(a)
#             second = tpl.index(a, first + 1) + 1
#             return tpl[tpl.index(a):second ]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (True, 11, " Python", [4,5,6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))
# t[4].append("Hi")
# print(t, id(t))


# Распаковка кортежа
# a = (1, 2, 3)
# x = a[0]
# y = a[1]
# z = a[2]
# x, y, z = a
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# #
# # first_name, year, married = user
#
# first_name, year, married = get_user()
#
# print(first_name)
# print(year)
# print(married)

# lst = [1, 2, 3, 4, 5]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))
# lst2.append(6)
# tpl2 = tuple(lst2)
# print(tpl2, type(tpl2))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")

# tpl = tuple(input("Введите строку: "))
# print(tpl)
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
# print(lst)
#
# for i in range(len(lst)):
#     print("Количество", lst[i], "=", tpl.count(lst[i]))

# import random
#
#
# def generate_tuple(a, b):
#     return tuple(random.randint(a, b) for i in range(10))
#
#
# tpl1 = generate_tuple(0, 5)
# tpl2 = generate_tuple(-5, 0)
#
#
# tpl3 = tpl1 + tpl2
#
# zero_count = tpl3.count(0)
#
# print(tpl1)
# print(tpl2)
# print(tpl3)
# print("0 =", zero_count)


# lst = [10, 2, 2, 2, 2, 3, 3, 8, 8, 9, 9, 9, 10]
# # st = {i for i in lst if i % 2 == 0}
# # lst2 = list(st)
# # print(lst2)
# st = set(lst)
# print(st)

# t = {'red', 'yellow', 'green'}
# print("green" in t)
# print("blue" in t)


# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print({i for i in lst if 'a' in i})
# print(tuple("A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst))
# print(["A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'])
#
#
# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print({i for i in lst if 'a' in i})
# print(tuple("A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst))
# print(["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"])
# # Вариант 2 (привычный код)
# lst2 = []
# for i in lst:
#     if i[1] == "c":
#         if i[0] == "a":
#             lst2.append("A" + i[1:])
#         else:
#             lst2.append("B" + i[1:])
# print(lst2)

# a = {'red', 'yellow', 'green'}
# print(a)
# a.add("black")
# print(a)
# a.remove('yellow')
# print(a)
# # a.remove('blue')
# # print(a)
# el = 'green'
# if el in a:
#     a.remove(el)
#
# print(a)

# a.discard('blue') # Удаляет элемент по значению
# print(a)

# a.clear() # Удаляет множество
# print(a)
# a = {0, 1, 2, 3}
# b = {4, 2, 3, 1}
# c = a.union(b) # Прибавляет тип данных set a + b
# c = a | b # Прибавляет тип данных set a + b
# a |= b # Пересохраняет переменую a со значениями  a + b
# c = a & b # Возвращает множество являющееся пересечением множеств а и b
# c = a - b # Возвращает разность множества оставляет то что остается
# c = a ^ b
# print(c)

#
# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print("Кол-во уникальных элементов:", len(s))
# print("Min:", min(s))
# print("Max:", max(s))

# s1 = "Hello"
# s2 = "How are you"
#
# a = set(s1) & set(s2)
# print(a)
#
# for i in a:
#     print(i, end=" ")

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a >= b
# print(c)

# a = frozenset([1, 2, 3, 4])
# print(a)

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
# print(lst[1])
# lst[1] = "ten"
# print(d["second"])
# d["second"] = "ten"

# a = dict() или {} # пустой словарь

# d = dict(a="Hello", b="World")
# print(d)
# print(type(d))
# d1 = {"a": "Hello", "b": "World"}
# print(d)

# d = {0: "text", "one": 45, (1, 2): [2, 3, 4, 5], 42: [9, 8], True: 1}
# print(d)


# s1 = input("Введите первую строку: ")
# s2 = input("Введите вторую строку: ")
# s3 = set(s1) - set(s2)
# print("Искомыми значениями являются: ", end="")
# for i in s3:
#     print(i, end=" ")


# d = {i: i ** 2 for i in range(1, 8)}
# print(d)
#
# # print(3 in d)
# # print(25 in d)
# key = 9
# # if key in d:
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
# print(res)

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)

# d = {i: input("->") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-5330', 3, 8500],
#     '3': ['AMD-4330', 5, 4500],
#     '4': ['Core-i7-4333', 4, 6500],
#     '5': ['Core-i3-3330', 7, 6500],
# }
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение некорректно введите число")
#         else:
#             print("Такого ключа нет")
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб.", sep="")

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
#
# print(d.keys())  # Список ключей
# print(d.values())  # Список значений
# print(d.items())  # Список ключей и значений в виде кортежа
#
# for i, j in d.items():
#     print(i, ":", j)

# d = {"A": 1, "B": 2, "C": 3}
# d2 = d.copy()  # Копия словаря
# print("D =", d)
# print("D2 =", d2)
# d2["B"] = 5
# print("D =", d)
# print("D2 =", d2)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# d.clear()  # Удаляет все элементы из словаря
# print(d)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # item = d.pop("M", "Такого ключа не существует в словаре")  # Удаляет элемент по заданному ключу, возвращает значение
# item = d.popitem()  # Удаляет последний элемент, возвращает кортеж из ключа и значения
# print(d)
# # print(item)
# print(d)
# value = d.get("W", "Такого ключа нет")
# print(value)
# item = d.setdefault("B", 5) # по заданному ключу устанавливает ключь и значение если ключа не существует
# print(d)
# print(item)
# d2 = {"R": 7, "Q": 9, "B": 5}
# d3 = [("M", 7), ("S", 9)]
#
# print(d)
# print(d2)
# # d3 = d | d2
# d.update(d2)
# d.update(d3)
# print(d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
#
# new_d = dict()
# new_d["name"] = d.pop("name")
# new_d["salary"] = d.pop("salary")
# print(d)
# print(new_d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# d['location'] = d.pop('city')
# print(d)

# d= {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three",
#     }, "second": {
#         4: "four",
#         5: "five",
#     }
# }
# print(d)
#
# # for x in d:
# #     print(x)
# #     for y in d[x]:
# #         print("\t", y, ": ", d[x][y], sep="" )
#
# for x, y in d.items():
#     print(x)
#     for i, j  in y.items():
#         print("\t", i, ": ", j, sep="")

# d = {
#     "John": {
#         "N": 3056,
#         "S": 8463,
#         "E": 8441,
#         "W": 2694
#     }, "Tom": {
#         "N": 4832,
#         "S": 6786,
#         "E": 4737,
#         "W": 3612
#     }, "Anne": {
#         "N": 5239,
#         "S": 4802,
#         "E": 5820,
#         "W": 1859
#     }, "Fiona": {
#         "N": 3904,
#         "S": 3645,
#         "E": 8821,
#         "W": 2451
#     },
# }
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ": ", d[x][y], sep="")
#
# name = input("Введите имя: ")
# region = input("Введите регион (N, S, E, W): ")
# if name in d and region in d[name]:
#     print("Текущий объем продаж:", d[name][region])
#     new_value = int(input("Введите новое значение: "))
#     d[name][region] = new_value
#     print("Новые данные по продажам. Имя:", name, ":", d[name])


# d = {"Один": 1, "Два": 2, "Три": 3, "Четыре": 4}
# # print({v: k for k, v in d.items()})
# print({k: v for k, v in d.items() if v <= 2})
# # print({k: k for k in d.items()})

# d = {i: i * 5 for i in
#      [10, 20, 30, 40, 50]}  # {10: 50, 20: 100, 30: 150, 40: 200, 50: 250}
# print(d)
# s = "Hello"
# d1 = {i: i * 3 for i in s} # {'H': 'HHH', 'e': 'eee', 'l': 'lll', 'o': 'ooo'}
# print(d1)

# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
# for i in lst: # 1
#     if type(i) is str: # type(i) == str
#         d[i] = []
#         s = i # s = "one"
#     else:
#         d[s].append(i)
#
# print(d)

# Функция Zip Объединяет несколько последовательностей в одну
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# d1 = list(zip([1, 2, 3], ['one', 'two', 'three'], [True, False, True]))
# print(d1)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = {k: v for k, v in zip(a, b)}
# print(d)

# a =[1,2,3]
# c = list(zip(a))
# print(c)

# one = {"name": "igor", "surname": "Pavlov", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Vetrova", "job": "Manager"}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2 )

# lst = [(1, 'a'), (2, 'b'), (3, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*lst)
# print(a)
# print(b)

# letter = ['b', 'a', 'd', 'c']
# numbers = [3, 4, 1, 2]
# d = dict(zip(letter, numbers))
# print(d)
# data = sorted((zip(letter, numbers)))
# print(data)

# data1 = list(zip(letter, numbers))
# print(data1)
# data1.sort()
# print(data1)
#
# d2 = dict(data1)
# print(d2)
#
#
# data2 = list(zip(numbers,letter))
# print(data2)
# data2.sort()
# print(data2)
#
# d3 = {v: k for k, v in data2}
# print(d3)

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]  # *- в данном случае распаковывает значение
# print(b)

# one = {'один': 1, "два": 2}
# two = {'три': 3, "четыре": 4}
# print({**one, **two})  # {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}

# colors = ["red", "yellow", "green"]
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1
# print()
# for j, color in enumerate(colors, 10):
#     print(j, ") ", color, sep="")

# d = {'один': 1, "два": 2, 'три': 3, "четыре": 4}
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ") ", k, ": ", v, sep="")

# def func(*args):
#     return args
#
# print(func(5))
# print(func(1,2,3))

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1,2,3,4,5,6,7,8,9))
# print(summa(7,8,9))

# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#
#     return res
#
#
# print(average(1,2,3,4,5,6,7,8,9))
# print(average(3,6,1,9,5))

# def func(a, b, *args):
#     return a, b, args
#
#
# print(func(5))
# print(func(1, 2, 3, 4, 5))

# def scores(student, *score):
#     print("student Name:", student)
#     for i in score:
#         print(i)
#
#
# scores("Igor", 5,5,4,3,3,5)
# scores("Ivan", 2,5,4,4,3,5)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func(st="Python"))


# def info(**data):
#     for k, v in data.items():
#         print(k, ":", v)
#     print()
#
# info(name="Irina", surname="Vetrova", age = 22)
# info(name="Igor", phone="12321321", surname="Petov", age = 22, email="asdasd,asd.ru")

# student = {}
# s = 0
# n = int(input("Кол-во студентов: "))
# for i in range(n):  # 0 1 2
#     name = input(str(i + 1) + "-й студент:")
#     point = int(input("Балл: "))
#     student[name] = point
#     s += point  # s = s + point
#
# average = s / n
# # print(student)
# print("Средний бал: ", round(average), ".Студенты с балом выше среднего: ", sep="")
#
# for i in student:
#     if student[i] > average:
#         print(i)

# def func1(*args):
#     print("args: ", args)
#     print(args[0])
#
#
# def func2(**kwargs):
#     print("kwargs: ", kwargs)
#     print(kwargs['one'])
#
#
# func1(1,2,3,4,5,6)
# func2(one=123, two=456)

# name = "Tom" # Глобальная переменная


# def hi():
#     global name
#     name = "Sam"
#     suname = "Jonson" # Локальная переменная
#     print("Hello", name, suname)
#
#
# def bye():
#     global name
#     name = "Igor"
#     print("Good bye", name)
#
#
# # print(name)
# hi()
# bye()
# print(name)
#

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# sum = 5

# lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(sum(lst))


# x = 4


# def func():
#     x = 2
#
#     def inner():
#         print("x =", x)
#         print(x + 3)
#
#     inner()
#
#
# func()

# Вложенные функции

# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма:", a + b)
#
#     print("a:", a)
#     fun2(3)
#
#
# fun1()


# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#     def  inner():
#         nonlocal a
#         a = 35
#         print("a =", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)

# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             global x
#             x = 55
#
#         fn3()
#         print("fn2.x = ", x)
#
#     fn2()
#     print("fn1.x = ", x)

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a)
#         print(b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# func1 = outer(5)
# print(func1(10))
#
# func2 = outer(6)
# print(func2(10))


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#
#     return func2


# def func(city):
#     n = 0
#     def inner():
#         nonlocal n
#         n += 1
#         print(city, n)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res1()

# Анонимные функции (Lambda выражения)

# def func(x, y):
#     return x + y
#
#
# print(func(1, 2))
# 1

# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# # 2
# print(func(1, 2))
# # 3
# func = (lambda x, y: x + y)(1, 2)
# print(func)

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())

# print((lambda *args: sum(args))(1, 2, 3, 4))

# tpl = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
#
# for t in tpl:
#     print(t("abc___"))

# # 1
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(42)
# print(f(3))
#
#
# # 2
# def outer(n):
#     return lambda x: n + x
#
#
# f = outer(42)
# print(f(3))
# # 3
# outer = lambda n: lambda x: n + x
# f = outer(42)
# print(f(3))
# # 4
# print((lambda n: lambda x: n + x)(42)(3))

# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))

# def func(i):
#     return i[1]
#
#
# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)
# print(dict(lst))

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)

# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(lst[3](12, 6))
#
# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
# d[2]()

# print((lambda a, b: a if a > b else b)(5, 13))
# print((lambda lst: [i * 2 for i in lst])([1, 2, 3, 4, 5, 6]))

# map(function, iterables), filter(function, iterables)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
# print(tuple(map(mult, lst)))

# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))

# t = (2.88, - 1.75, 100.55)
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))
# print(tuple(map(round, t)))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(dict(map(lambda x, y: (x, y), st, num)))
# print(list(map(lambda x, y: (x, y), st, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda a, b: a + b, l1, l2)))

# lst = [input("->") for i in range(5)]
# print(lst)
# lst = list(map(int, lst))
# print(lst)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(tuple(filter(lambda s: len(s) == 3, t)))

# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# lst2 = list(filter(lambda s: s > 75, lst))
# print(lst)
# print(lst2)


# from random import randint
#
# lst = [randint(1,  40) for i in range(10)]
# print(lst)
#
# print(list(filter(lambda a: (a >= 10) and a <= 20, lst)))
# print(list(filter(lambda a: 10 <= a <= 20, lst)))

# nums = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: s % 15 == 0, nums)))
# print(list(filter(lambda s: not s % 15, nums)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))
# # или
# print([x ** 2 for x in range(10) if x % 2])

# import math
# from math import pi
#
# area = {'Circle': lambda a: (a ** 2) * pi, 'Rectangle': lambda a, b: a * b,
#         'Trapezoid': lambda a, b, h: (a + b) / 2 * h}
#
#
# print("Площадь окружности радиуса 2: ", area['Circle'](2))
# print("Площадь прямоугольника размером 10Х13: ", area['Rectangle'](10, 13))
# print("Площадь трапеции для a=7, b=5, h=3: ", area['Trapezoid'](7, 5, 3))

# Декораторы

# def hello():
#         return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#         print("Hello, I am func 'super_func'")
#         print(func())
#
#
# super_func(hello)

# def hello():
#         return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#
#     return func_wrapper
#
# @my_decorator # Декоратор
# def func_test(): # Декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(func):
#     def wrap():
#         return "<i>" + func() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def outer(fn):
#     def inner(args1, args2):
#         print("Данные:", args1, args2)
#         fn(args1, args2)
#
#     return inner
#
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")


# def outer(fn):
#     def inner(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(15, 12)

# def multiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return my_decorator
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print("Результат:", return_num(5))


# Строки

# print(bin(18))  # 0b10010 - двоичная система счисления
# print(oct(18))  # 0o22 - восьмеричная система счисления
# print(hex(18))  # 0x12 - шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010 + 4)

# Unicode

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print("y" in e)
# print("a" in e)
# print(e[-1])
# print(e[1:3])

#

# print(u"Привет")
# print("Привет")

# print("C:\\file.txt\\")
# print(r"C:\file.txt\\"[:-1])
# print(r"C:\file.txt" + "\\")

# def avg(fn):
#     def wrap(*args):
#         st = ""
#         for i in args:
#             st += str(i) + ", "
#         print("Среднее арифметическое:", st[:-2], "=", fn(*args) / len(args))
#
#     return wrap
#
#
# @avg
# def summa(*args):
#     st = ", ".join(map(str, args))
#     print("Сумма чисел:", st, "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)


# print(b"a1b2c2")


# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")


# x = 10
# y = 5
# print(f"{x=}, {y=}")
# # print("x=", x, ", y=", y, sep="")
#
# print(f"{x} x {y} / 7 = {round(x * y / 7, 2)}")
# print(f"{x} x {y} / 7 = {x * y / 7:.3f}")

# num = 74
# print(f"{{{{{num}}}}}")
#
# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)
#
#
# st = ("Однострочный "
#       "текст")
# print(st)
#
# s = """Многострочный
# текст
# """
# print(s)
#
# s1 = '''Многострочный
# текст
# '''
# print(s1)
#
#
# """Многострочный комментарий
# текст
# """
#
# "Однострочный комментарий"


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n ** 2
#     return res
#
#
# print(square(5))
# print(square.__doc__)
# print(len.__doc__)
# print(min.__doc__)
# print(max.__doc__)
# print(sum.__doc__)


# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('a'))
# print(ord('#'))
# print(ord('п'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))
# print(chr(344))

# a = 97
# b = 122
#
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")


# from random import randint
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Случайный пароль:", random_password())

# print(dir(str))

s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
#
# print(s.count("h", 1, -4))
# print(s.lower().count("i"))
# #
# print(s.find("Python"))
# print(s.find("h", 1, -4))
# print(s.find("h"))
# print(s.rfind("h"))
# #
# print(s.index("h", 1, -4))
# print(s.rindex("h"))

# # st = "один два"
# st = input("-> ")
# one = st[:st.find(" ")]  # st[:4]
# two = st[st.find(" ") + 1:]  # st[4:]
# res = two + " " + one
# print(res)

# st = "один два"
# print(st[st.find(" ") + 1:] + " " + st[:st.find(" ")])

# s = "hello, WORLD! I am learning Python."
# print(s.startswith("hello"))
# print(s.startswith("I am", 14))
# print(s.find("I am"))
#
# print(s.endswith("Python."))


# print("abc123".isalnum())  # состоит ли строка из букв и цифр
# print("abc!123".isalnum())
# print("abc".isalnum())
# print("123№".isalnum())

# print("ABCabcП".isalpha())  # состоит ли строка из букв
# print("ABC%abc".isalpha())
#
# print("123".isdigit())  # # состоит ли строка из цифр
# print("123@".isdigit())


# print('aab'.islower())  # находятся ли в строке буквы в нижнем регистре, допускается наличие других символов
# print('123aab!№;'.islower())
#
# print("ABC".isupper())  # находятся ли в строке буквы в верхнем регистре, допускается наличие других символов
# print("123AвBC!!".isupper())

# print("py".center(10))
# print("py".center(10, "-"))
# print("py".center(1))


# print("    py".lstrip())
# print("py    ".rstrip())
# print("    py    ".strip())

# print("https://www.python.org".lstrip("/:htps"))
# print("https://www.python.org.www".lstrip("/:htps").rstrip(".w"))
# print("https://www.python.org.www".strip("/:htps.w"))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("Nython", "Python", 2))


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '99']))
#
# print(":".join("Hello"))

#
# s = "Hello"
# print(s[::-1])


# s = "I am learning Python. hello WORLD!"
# h1 = s.find("h")
# h2 = s.rfind("h")
# s1 = s[:h1+1] + s[h1+1:h2][::-1] + s[h2:]
# print(s1)

# # s = "I am learning Python. hello, WORLD!"
# s = input("Введите строку: ")
# # print(s.rfind('h') + 1)
# a = s[:s.find('h')]  # s[:17]
# b = s[s.find('h'):s.rfind('h') + 1]  # s[17:23]  # hon. h
# c = s[s.rfind('h') + 1:]  # s[23:]
# print(a + b[::-1] + c)


# print("Строка разделенная пробелами".split())
# print("www.python.org.ru".split(".", 2))


# s = input("Введите ФИО: ").split()
# print(s)
# print(f"{s[0]} {s[1][0]}. {s[2][0]}.")


# s = input("Введите числа через пробел: ").split()
# print(s)
# num = list(map(int, s))
# print(num)
# print(sum(num))


# Регулярные выражения

import re

s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel_lo] Wor-ld 200000000000000"
# # print(dir(re))
# # reg = "\\."
# reg = r"\."
# print(re.findall(reg, s))  # возвращает список совпадений с шаблоном
# print(re.search(reg, s))  # возвращает только первое совпадение с шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.split(reg, s))  # возвращает список, который разбит по заданному шаблону
# print(re.sub(reg, "!", s))  # поиск и замена

# reg = r"[205]"
# reg = r"[0-9]"
# reg = r"[12][0-9][0-9][0-9]"
# reg = r"[а-яА-Я]"
# reg = r"[А-яЁё.\]\[-]"
# reg = r"[A-Za-z]"
# reg = r"[^0-9]"
# print(re.findall(reg, s))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T19:49. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))
# reg = r"\d"  # [0-9]
# reg = r"\D"  # [^0-9]
# reg = r"\s"  # [ ]
# reg = r"\S"  # [^ ]
# reg = r"\w"  # [А-яA-Za-z0-9_]
# reg = r"\W"  # [^А-яA-Za-z0-9_]
# reg = r"\AЯ ищу"
# reg = r"Wor-ld\Z"
# reg = r"\Bния"
# reg = r"\w+"
# reg = r"20*"
# print(re.findall(reg, s))

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1 повторения

# d = "Цифры: 7, +17, --42, 0013, 0.3"
# reg = r"[+-]?[\d.]+"
# print(re.findall(reg, d))

# st = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s#.+", "", st))
# print(re.sub("-", ".", st))
#
# print("Дата рождения:", re.sub(r"\s#.+", "", re.sub("-", ".", st)))

# st = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# reg = r"\w+\s*=\s*\w+\s*\w*\.?\w*\.?"
# reg = r"\w+\s*=\s*\w+[\s\w.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
# print(re.split(r";\s", st))


# st = "12 сентября 2025 год 456 789456123"
# # reg = r"\d{4}"
# reg = r"\d{2,4}"
# # reg = r"\d{,4}"
# # reg = r"\d{4,}"
# print(re.findall(reg, st))


# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))

# reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))

# def validate_login(login):
#     return re.findall(r"^[a-zA-Z0-9_-]{3,16}$", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("Pyt"))

# st = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# reg = r"[0-9A-zА-я@.-]+"
# print(re.findall(reg, st))


import re

# from tkinter.font import names

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
# #
# text = "hello world"
# print(re.findall(r"\w\+", text))
# print(re.findall(r"\w\+", text, re.DEBUG))

# text = "helLo worLd"
# print(re.findall(r"l", text, re.IGNORECASE))


# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))
#
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+  # part 1
# @         # @
# [a-z.]+   # part 2
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON
# """
# reg = "(?mi)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))
#
#
# st = "12 сентября 2025 год 456 789456123"
# # reg = r"\d{4}"
# # reg = r"\d{2,4}?"
# # reg = r"\d{,4}?"
# reg = r"\d{4,}?"
# print(re.findall(reg, st))
#
# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Василий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0, int"
# # reg = r"int\s*=\s*\d[\w.]*|float\s*=\s*\d[\w.]*"
# reg = r"(?:int|float)\s*=\s*\d[\w.]*"
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))

# s = "5 + 7*2 - 4"
# reg = r"\s*[+*-]\s*"
# print(re.split(reg, s))
#
# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))


# s = "18-01-2021"  # 1900-2099
# reg = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# print(re.search(reg, s))
# print(re.search(reg, s).group())


# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE).group())
# m = re.search(reg, s, re.IGNORECASE)
# print(m[1])
# print(m[2])
# print(m[0])

# s = "Самолет прилетает 10/23/2025. Будет рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))


# Рекурсия

# def elevator(n):  # 0
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # стек 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


#

# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def to_str(n, base):  # n = 15, base = 16
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 'F' + 'E'
#
#
# print(to_str(254, 16))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

#
# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):  # ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
#     count = 0  # 10
#     for item in item_list:  #
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def finding_negative(n):
#     if not n:
#         return 0
#     c = 0
#     if n[0] < 0:
#         c += 1
#     return c + finding_negative(n[1:])
#
#
# numbers = [-2, 3, 8, -11, -4, 6]
#
#
# print(f'n = {finding_negative(numbers)}')

# print("Текст в локальном репозитории")

# print("Код написан на новом репозитории")

# Файлы

# f = open("text.txt")
# f = open(r"C:\Users\AndreyVasilev\Desktop\python\text.txt")
#
# print(*f)
# print(f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# print(f.closed)


# f = open("text.txt", "r")
# print(f.read(3))
# print(f.read())
#
# f.close()


# f = open("xyz.txt", 'w')
# f.write("This is line1.\nThis is line2.\nThis is line3.\n")
# f.close()


# f = open("xyz.txt")
# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# print(f.readlines(15))
# print(f.readlines())
# f.close()


# f = open("xyz.txt")
# for line in f:
#     print(line)
# f.close()

# lines = ["This is line1.\n", "This is line2.\n", "This is line3.\n"]

# f = open("lines.txt", "w")
# f.writelines(lines)
# f.close()

# lines = [str(i) for i in range(10, 1000, 15)]
# print(lines)
#
# # lines = ["This is line1.\n", "This is line2.\n", "This is line3.\n"]
# f = open("lines.txt", "w")
# for index in lines:
#     f.write(index + "\t")
# f.close()
# file = "text2.txt"
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
#
# f.close()
#
# f = open(file, "r")
# read_line = f.readlines()
# print(read_line)
# read_line[1] = "Hello world\n"
# print(read_line)
# f.close()
#
# f = open(file, "w")
# f.writelines(read_line)
# f.close()

# f = open("text.txt", "r")
# print(f.read(3))
# print(f.tell()) # Возращает текущую позицию условного курсора в файле
# print(f.seek(1)) # Перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("text5.txt", "a")
# print(f.write("I am learning Python"))
# print(f.seek(0))
# print(f.write("--new string--"))
# # print(f.read())
# f.close()

# with open("text.txt", "w") as f:
#     print(f.write("0123456789"))
# print(f.closed)

# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.04]
#
#
# def get_line(lt):
#     lt = list(map(str,lt))
#     return " ".join(lt)
#
#
# with open("res.txt", "w") as f:
#     f.write(get_line(lst))
#
# print("Конец программы")


# with open("res.txt") as f:
#     nums = f.read()
#
# print(nums)
#
# print(sum(map(float, nums.split())))
# print(sum(list(map(float, nums.split()))))


# with open("res2.txt", "w") as f:
#     f.write("Файл - именованная область данных на носителе информации используемая как базовый обьект  "
#             "с данными в операционных системах.")  # взаимодействия
#
#
# def longest_words(file):
#     with open(file) as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         return res
#
#
# print(longest_words("res2.txt"))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# with open("one.txt", "w") as f:
#     f.write(text)
#
# with open("one.txt", "r") as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("Строка","Линия -")
#         fw.write(line)

import os

# print(os.getcwd()) # Путь к текущей директории
#
# print(os.listdir()) # Возвращает список директорий и файлов
# print(os.listdir(".."))

# os.mkdir("folder") # Создать папку

# os.rmdir("folder") # Удалить папку

# os.makedirs("nested1/nested2/nested3")  # Создает директорию спромежуточными папками

# os.remove("xyz.txt") # Удаляет файл

# os.rename("two.txt", "www.txt") # Переименовывает файл
#
# os.rename("www.txt", "nested1/nested2/nested3/www.txt") # Перемещает файл в  заданную папку

# os.renames("text4.txt", "test/text4.txt") # Переместили файл создавая промежуточные папки

# print(os.walk("nested1"))
# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("\tdirs:", dirs)
#     print("\tFiles", files)

# import os.path

# print(os.path.split(r"C:\Users\AndreyVasilev\Desktop\python\nested1\text5.txt"))
#
# print(os.path.join(r"C:\Users", "AndreyVasilev", "python"))

import os

# dirs = [r"Word\F1", r"Word\F2\F21"]
# # for d in dirs:
# #     os.makedirs(d)
#
# files = {
#     "Word": ["w.txt"],
#     r"Word\F1": ["f11.txt", "f12.txt", "f13.txt"],
#     r"Word\F2\F21": ["f211.txt", "f212.txt"]
# }
#
# for d, files in files.items():
#     for file in files:
#         file_path = os.path.join(d, file)
#         # print(file_path)
#         open(file_path, "w").close()
#
# file_with_text = [r"Word\w.txt", r"Word\F1\f12.txt", r"Word\F2\F21\f211.txt", r"Word\F2\F21\f212.txt"]
#
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"Какой-то текст в файле {file}")
#
# def print_three(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, directory, file_name in os.walk(root, topdown):
#         print(root)
#         print(directory)
#         print(file_name)
#     print("-" * 50)
#
#
# print_three("Word", False)
# print_three("Word", True)


# print(os.path.exists(r"C:\Users\AndreyVasilev\Desktop\python\nested1\text5.txt"))
# print(os.path.isfile(r"C:\Users\AndreyVasilev\Desktop\python\nested1\text5.txt"))
# print(os.path.isdir(r"C:\Users\AndreyVasilev\Desktop\python\nested1"))

# import  os
# import time
#
# print(os.path.getsize("one.txt")) # Размер файла в байтах
# print(os.path.getatime("one.txt")) # Время последнего доступа к файлу
# print(os.path.getmtime("one.txt")) # Время последнего изменения файла
# print(os.path.getctime("one.txt")) # возвращает время создания файла
#
# kb = os.path.getsize("one.txt")
# a = os.path.getatime("one.txt")
# m = os.path.getmtime("one.txt")
# c = os.path.getctime("one.txt")
#
# print(time.strftime("%d.%m.%y, %H:%M:%S", time.localtime(a))) # Переводим секунды
# print(time.strftime("%d.%m.%y, %H:%M:%S", time.localtime(m)))
# print(time.strftime("%d.%m.%y, %H:%M:%S", time.localtime(c)))
# print(kb // 1024)


# class Point:
#     x = 1
#     y = 2

#
# p1 = Point()
# p1.x = 10
# p1.y = 20
# # Point.x = 100
# print(p1.x, p1.y)
# print(p1.__dict__)
#
# p2 = Point()
# print(p2.x, p2.y)
# p2.x = 5
# print(p2.__dict__)
#
# print(Point.__dict__)


# class Point:
#     """Класс для предоставлении координат точек на плоскости"""
#     x = 1
#     y = 2
#
#     def set_coord(self, x1, y1):
#         self.x = x1
#         self.y = y1
#
#
# p1 = Point()
# print(Point.__doc__)
# print(Point.__dict__)
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# print(p1.__dict__)
# Point.set_coord(p1, 20, 30)
# print(p1.__dict__)
#
#
# p2 = Point()
# p2.set_coord(100,200)
# print(p2.__dict__)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # устанавливаем новое имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())

# class Person:
#     skill = 10
#     name = ""
#     surname = ""
#
#     def __init__(self, name, surname):  # инициализатор
#         self.name = name
#         self.surname = surname
#         # print("Инициализатор для", self.name, self.surname)
#
#     def __del__(self):
#         print("Удаление экземпляра")
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
#
# del p1
# print()
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot("PC-3O")
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим.")
#
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов:", Robot.k)


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def get_coord_x(self):
#         return self.__x
#
#     def get_coord_y(self):
#         return self.__y
#
#
# p1 = Point(5, "10")
# # print(p1.__dict__)
# # p1.z = 20
# # print(p1.__x, p1.__y)
# # p1.__x = 50
# # p1.__y = "abc"
# p1.set_coord(5.2, 100)
# print(p1.get_coord())
# p1.set_coord_x(10)
# p1.set_coord_y(50)
#
# p1._Point__x = "abc"
# print(p1._Point__x = 10)
# print(p1.__dict__)

import os
import time

#
# file_path = "nested1\\nested2\\test3.txt"
#
# if os.path.exists(file_path):
#     directory, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     t = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime))
#     print(f"{name} ({directory}) - время последнего доступа к файлу {t}")
# else:
#     print(f"Файл {file_path} не существует")


#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimeter(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         # for i in range(self.__length):
#         #     for j in range(self.__width):
#         #         print("*", end="")
#         #     print()
#
#         # for i in range(self.__length):
#         #     print("*" * self.__width)
#
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# r1 = Rectangle(4, 12)
# r1.set_width(9)
# r1.set_length(3)
# print("Длина прямоугольника:", r1.get_length())
# print("Ширина прямоугольника:", r1.get_width())
# print("Площадь прямоугольника:", r1.get_area())
# print("Периметр прямоугольника:", r1.get_perimeter())
# print("Гипотенуза прямоугольника:", r1.get_hypotenuse())
# r1.get_draw()


# class Point:
#     __slots__ = ["x", "y", "z"]
#
#     def __init__(self, x1, y1):
#         self.x = x1
#         self.y = y1
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.x, p1.y, p1.z)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def __set_coord_x(self, x):
#         # print("Вызов __set_coord_x")
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Неверный формат данных")
#
#     def __get_coord_x(self):
#         # print("Вызов __get_coord_x")
#         return self.__x
#
#     def __del_coord_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# # print(p1.__set_coord_x(50))
# # print(p1.__get_coord_x())
# p1.x = 50  # set
# print(p1.x)  # get
# del p1.x  # del
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @staticmethod
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Неверный формат данных")
#
#     @x.deleter
#     def x(self):
#         del self.__x
#
#     # x = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# p1.x = 50  # set
# print(p1.x)  # get
# del p1.x  # del
# print(p1.__dict__)


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.__old = year
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# p1.old = 31
# print(p1.__dict__)
# # del p1.name
# del p1.old
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# p4 = Point()
#
# print(Point.get_count())
# print(p1.get_count())
#
#
# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))
#
# #
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# ch = Change()
# print(ch.inc(10), Change.dec(10))


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a  # mx = 3
#         if b > mx:  # 5 > 3
#             mx = b  # mx = 5
#         if c > mx:  # 7 > 5
#             mx = c  # mx = 7
#         if d > mx:  # 9 > 7
#             mx = d  # mx = 9
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]  # 3
#         for i in args:
#             if i < mn:  # 9 < 3
#                 mn = i
#         return mn
#
#     @staticmethod
#     def average(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def average(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print("Максимальное число:", Numbers.max(3, 5, 7, 9))
# print("Минимальное число:", Numbers.min(3, 5, 7, 9))
# print("Среднее арифметическое:", Numbers.average(3, 5, 7, 9))
# print("Факториал числа:", Numbers.factorial(5))

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))  # [23, 01, 2025]
#         date = cls(day, month, year)  # d = Date(day, month, year)
#         return date
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # string_date = "23.01.2025"
# # day, month, year = map(int, string_date.split("."))  # [23, 01, 2025]
# # d = Date(day, month, year)
# d = Date.from_string("23.01.2025")
# print(d.string_to_db())
#
# d1 = Date.from_string("15.12.2024")
# print(d1.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете: ")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#

# acc = Account("12345", "Долгих", 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

#
# from math import sqrt
#
#
# class Area:
#     __count = 0
#
#     @staticmethod
#     def triangle_area(a, b, c):
#         p = (a + b + c) / 2
#         Area.__count += 1
#         return sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area_2(a, h):
#         Area.__count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.__count += 1
#         return a ** 2
#
#     @staticmethod
#     def rectangle_area(a, b):
#         Area.__count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.__count
#
#
# print("Площадь треугольника по формуле Герона (3,4,5):", Area.triangle_area(3, 4, 5))
# print("Площадь треугольника по формуле Герона (13,14,15):", Area.triangle_area(13, 14, 15))
# print("Площадь треугольника через основание и высоту (6,7):", Area.triangle_area_2(6, 7))
# print("Площадь квадрата (7):", Area.square_area(7))
# print("Площадь квадрата (8):", Area.square_area(8))
# print("Площадь квадрата (9):", Area.square_area(9))
# print("Площадь прямоугольника (2, 6):", Area.rectangle_area(2, 6))
# print("Количество подсчетов площади:", Area.get_count())


# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич!!!']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or not 14 <= old <= 100:  # old < 14 or old > 100
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Ветров Игорь Николаевич"
# print(p1.fio)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# print(Point.__dict__)
# print(issubclass(Point, object))
# print(type(5))

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "green", 5)
# line.draw_line()
#
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if isinstance(w, int) and w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if isinstance(h, int) and h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть положительным числом")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
#
# print(rect.area())
# print(rect.__dict__)


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     ...
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px", "solid", "red")
# shape2.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)  # "1 2 3"
# print(type(v))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x=None, y=None):
#         if y is None:
#             self.x = x
#         elif x is None:
#             self.y = y
#         else:
#             self.x = x
#             self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p1.set_coord(20, 30)
# print(p1.__dict__)
# p1.set_coord(50)
# print(p1.__dict__)
# p1.set_coord(y=100)
# print(p1.__dict__)

# Абстрактные методы

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Prop:
#     def __init__(self, sp, ep, color, width):
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     ...
#     # def draw(self):
#         # print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# shapes = list()
# shapes.append(Line(Point(0, 0), Point(10, 10), "yellow", 10))
# shapes.append(Line(Point(10, 10), Point(20, 20), "red", 6))
# shapes.append(Rect(Point(50, 50), Point(70, 70), "blue", 4))
# shapes.append(Ellipse(Point(80, 80), Point(100, 100), "green", 3))
#
# for i in shapes:
#     i.draw()

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную доску")
#
#     @abstractmethod
#     def move(self):
#         # print("Метод move() в базовом классе")
#         pass
#
# class Queen(Chess):
#
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
# #
# #
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):  # 20, None, None
#         if radius is None:
#             if length is None:
#                 self.width = self.length = width
#             else:
#                 self.width = width
#                 self.length = length
#         else:
#             self.radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class RectangleTable(Table):
#     def calc_area(self):
#         return self.width * self.length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = RectangleTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = RectangleTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def print_info(self):
#         self.print_value()  # Euro(5)
#         print(f"= {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# print("*" * 50)
# for elem in d:
#     elem.print_info()
#
# print("*" * 50)
# for elem in e:
#     elem.print_info()


# Интерфейсы

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#
#
# # c = Child()
# gc = GrandChild()
# gc.display1()
# gc.display2()


# Вложенные классы
#
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_static_method():
#         print("Статический метод")
#
#     def outer_obj_method(self):
#         print("Метод экземпляра", self.name)
#
#     class MyInner:
#         def __init__(self, inner_inner, obj):
#             self.inner_inner = inner_inner
#             self.obj = obj
#
#         def inner_method(self):
#             print("Метод внутреннего класса", MyOuter.age, self.obj.name)
#             print(self.inner_inner)
#             MyOuter.outer_static_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter("внешний")
# print(out.name)
# inner = out.MyInner("внутренний", out)
# # inner = MyOuter.MyInner("внутренний")
# print(inner.inner_inner)
# inner.inner_method()

# class LightColor:
#     def __init__(self):
#         self.name = "LightGreen"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = LightColor()
#         self.dg = self.DarkColor()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class DarkColor:
#         def __init__(self):
#             self.name = "DarkGreen"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# print(outer.name)
# g = outer.lg
# g.display()
# g1 = outer.dg
# g1.display()


# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i9"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)
# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(10, 20)
# # p1.z = 30
# # print(p1.__dict__)
# p1.length = 10
# print(p1.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(10, 20)
# p2 = Point2D(10, 20)
# print("p1 =", p1.__sizeof__())
# print("p2 =", p2.__sizeof__() + p2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 2, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)
# # print(pt3.__dict__)


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")
# dog.bark()
# dog.sleep()
# dog.play()


# class A:
#     def __init__(self):
#         print("Инициализатор класса A")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(A):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)


# class A:
#     def __init__(self):
#         print("Инициализатор класса A")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса AA")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#
#
# d = D()
# print(D.mro())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор класса Pos")
#         self.sp = sp
#         self.ep = ep
#         # Styles.__init__(self, *args)
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()

# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 17:15")
#
#
# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n2 = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# n2.save_sell_log()


# Перегрузка операторов

# Число секунд в одном дне: 24 * 60 * 60 = 86400

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
# #
# #
# c1 = Clock(100)
# c2 = Clock(200)
# c3 = c1 + c2
# print(c1.get_format_time())
# print(c2.get_format_time())
# c1 += c2
# print(c3.get_format_time())
# print(c1.get_format_time())
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")
#
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время равно")

# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # off = 10 + 1 - 5  => 6
#             self.marks.extend([None] * off)  # [5, 5, 3, 4, 5, None, None, None, None, None, None]
#
#         self.marks[key] = value  # [5, 5, 3, 4, 5, None, None, None, None, None, 4]
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# # print(s1.marks[2])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         if item == "min":
#             return (self.sec // 60) % 60
#         if item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(8000)
# print(c1.get_format_time())
# c1["hour"] = 10
# c1["min"] = 20
# c1["sec"] = 30
# print(c1["hour"], c1["min"], c1["sec"])

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(1, randint(2, 9))]  # range(1, 9)  # от 1 по 8
#         else:
#             raise TypeError("Type are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# # cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def perimeter(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def perimeter(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.perimeter())


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cat(Animal):
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     def make_sound(self):
#         print(f"{self.name} мяукает.")
#
#
# class Dog(Animal):
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     def make_sound(self):
#         print(f"{self.name} гавкает.")
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
#
# for animal in cat, dog:
#     animal.info()
#     animal.make_sound()

# from abc import ABC, abstractmethod
#
#
# class Human(ABC):
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     @abstractmethod
#     def info(self):
#         print(f"\n{self.surname} {self.name} {self.age}", end=" ")
#
#
# class Student(Human):
#     def __init__(self, name, surname, age, speciality, groups, rating):
#         super().__init__(name, surname, age)
#         self.speciality = speciality
#         self.groups = groups
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.groups} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, name, surname, age, subject, experience):
#         super().__init__(name, surname, age)
#         self.subject = subject
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"{self.subject} {self.experience}", end=" ")
#
#
# class Graduate(Student):
#     def __init__(self, name, surname, age, speciality, groups, rating, topic):
#         super().__init__(name, surname, age, speciality, groups, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}")
#
#
# group = [
#     Student("Даши", "Батодалаев", 16, "ГК", "Web_011", 5),
#     Student("Линар", "Загидуллин", 32, "РПО", "PD_011", 5),
#     Teacher("Андрей", "Даньшин", 38, "Астрофизика", 110),
#     Graduate("Сергей", "Шугани", 15, "PПО", "PD_011", 5,
#              "Защита персональных данных")
# ]
#
# for i in group:
#     i.info()


# Функторы

# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         print(self.count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()

# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1("   Hello World!  ...  "))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(self.chars)
#
#
# s2 = StringStrip("?:!.; ")
# print(s2("   Hello World!  ...  "))


# class StringStrip:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.chars)
#
#
# s2 = StringStrip("?:!.; ")
# print(s2("   Hello World!  ...  "))
# import geometry
# from abc import ABC, abstractmethod
#
#
# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def info(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, side, color):
#         super().__init__(color)
#         self.side = side
#
#     def get_perimeter(self):
#         return self.side * 4
#
#     def get_area(self):
#         return self.side * self.side
#
#     def draw(self):
#         return ("*  " * self.side + "\n") * self.side
#
#     def info(self):
#         print(f"=== Квадрат ===\nСторона: {self.side}\nЦвет: {self.color}"
#               f"\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width, color):
#         super().__init__(color)
#         self.length = length
#         self.width = width
#
#     def get_perimeter(self):
#         return (self.length + self.width) * 2
#
#     def get_area(self):
#         return self.length * self.width
#
#     def draw(self):
#         return ("*  " * self.width + "\n") * self.length
#
#     def info(self):
#         print(f"=== Прямоугольник ===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}"
#               f"\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")
#
#
# class Triangle(Shape):
#     def __init__(self, side_1, side_2, side_3, color):
#         super().__init__(color)
#         self.side_1 = side_1
#         self.side_2 = side_2
#         self.side_3 = side_3
#
#     def get_perimeter(self):
#         return self.side_1 + self.side_2 + self.side_3
#
#     def get_area(self):
#         p = self.get_perimeter() / 2
#         return round(geometry.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)), 2)
#
#     def draw(self):
#         # return ("*  " * self.width + "\n") * self.length
#         rows = []
#         for n in range(self.side_2):  # 6, n = 2
#             rows.append(" " * n + "*" * (self.side_1 - 2 * n))  # ['***********', ' *********', '  *******']
#         rows.reverse()
#         # return "\n".join(reversed(rows))
#         return "\n".join(rows)
#
#     def info(self):
#         print(f"=== Треугольник ===\nСторона 1: {self.side_1}\nСторона 2: {self.side_2}\nСторона 3: {self.side_3}"
#               f"\nЦвет: {self.color}\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")
#
#
# # sq = Square(3, "red")
# # sq.info()
# # rect = Rectangle(3, 7, "green")
# # rect.info()
# # tr = Triangle(11, 6, 6, "yellow")
# # tr.info()
#
# fig = [Square(3, "red"), Rectangle(3, 7, "green"), Triangle(11, 6, 6, "yellow")]
#
# for g in fig:
#     g.info()


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self):
#         print("Перед вызовом функции")
#         self.func()
#         print("После вызова функции")
#
#
# @MyDecorator
# def func():
#     print("text")
#
#
# func()
#
#
# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         return f"Перед вызовом функции \n{self.func(a, b)} \nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(2, 3))


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, *args, **kwargs):
#         return f"Перед вызовом функции \n{self.func(*args, **kwargs)} \nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a + b - c
#
#
# print(func(2, 5))
# print(func2(2, 5, 3))
# print(func2(c=2, a=5, b=3))


# class MyDecorator:
#     def __init__(self, arg):  # "test"
#         self.name = arg
#
#     def __call__(self, fn):  # func
#         def wrap(*args, **kwargs):  # 2, 5
#             print(self.name)
#             return f"Перед вызовом функции \n{fn(*args, **kwargs)} \nПосле вызова функции"
#
#         return wrap
#
#
# @MyDecorator("test")
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             return func(a, b) ** self.arg
#
#         return wrapper
#
#
# @Power(3)
# def multiply(a, b):
#     return a * b
#
#
# @Power(5)
# def multiply1(a, b):
#     return a + b
#
#
# print(multiply(2, 2))
# print(multiply1(3, 2))

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#     @dec
#     def method1(self, arg):
#         print("Вывод аргумента:", arg)
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()
# p1.method1("значение")

# Метаклассы

# a = 5
# print(type(a))
# print(type(int))


# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     "MyList",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst.append(9)
# print(lst, lst.get_length())

# Создание модулей

# import geometry.rect
# import geometry.sq
# import geometry.trian
#
# from geometry import *

# from geometry import rect, sq, trian


# if __name__ == "__main__":
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.perimeter())

# def ran():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.perimeter())
#
#
# if __name__ == "__main__":
#     ran()


# class Car:
#     def __init__(self, brand, model, year, mileage):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#
#
# class Electrocar(Car):
#     def __init__(self, brand, model, year, mileage, charge):
#         super().__init__(brand, model, year, mileage)
#         self.charge = charge
#
#     def __call__(self, *args, **kwargs):
#         print(f"{self.brand},{self.model},{self.year},{self.mileage}\n"
#               f"Этот автомобиль имеет мощность: {self.charge}%")
#
#
# tesla = Electrocar("Tesla", "T", "2008 год", "99000 km", 100)

# from Car.Electrocar import Electrocar
#
# tesla = Electrocar("Tesla", "T", "2008 год", "99000 km", 100)
# tesla()

import pickle

# file_name = "basket.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": ("морковь", "лук"),
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, "rb") as f:
#     shop_list2 = pickle.load(f)
#
# print(shop_list2)


# class Test:
#     num = 25
#     st = "Привет"
#     lst = [1, 2, 3]
#     tpl = (22, 33)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
# # print(obj)
#
# string = pickle.dumps(obj)
# print(string)
#
# string2 = pickle.loads(string)
# print(string2)


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()  # 35 test 4
# # print(item1)
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
#
# print(item3.__dict__)
# print(item3)


import json

# data = {
#     'name': 'Olga',
#     'age': 35,
#     "20": None,
#     "None": "no",
#     "True": False,
#     'hobbies': ('running', 'signing'),
#     'children': [
#         {
#             'firstName': 'Alice',
#             'age': 6
#         }
#     ]
# }

# with open("data_file.json", "w") as f:
#     json.dump(data, f, indent=4)
#
# with open("data_file.json", "r") as f:
#     data1 = json.load(f)
#
# print(data1)
#
# string = json.dumps(data, sort_keys=True)
# print(string, type(string))
# #
# data1 = json.loads(string)
# print(data1, type(data1))


# x = {"name": "Виктор"}
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))
#
# st = json.dumps(x)
# print(json.loads(st))


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# #
# #
# def write_json(person_dict):  # {'name': ..., 'tel': ...}
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#
#     with open("persons.json", "w") as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())

import json

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
# st = ''
# for i in self.marks:
#     st += str(i) + ", "
# return f"Студент => {self.name}: {st[:-2]}"
# st = ", ".join(map(str, self.marks))
# return f"Студент => {self.name}: {st}"
# return f"Студент => {self.name}: {", ".join(map(str, self.marks))}"

#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 1)
#
#     def get_file_name(self):
#         return self.name + ".json"  # 'Bodnya.json'
#
#     def dump_to_json(self):
#         data = {"name": self.name, "marks": self.marks}
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students):
#         self.students = students
#
#     def __str__(self):
#         st = "\n".join(map(str, self.students))
#         return f"{st}"
#
#
# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(4, 4)
# # print(st1)
# # print(st1.average_mark())
# # st1.dump_to_json()
# # st1.load_from_file()
# sts1 = [st1, st2]
# group1 = Group(sts1)
# print(group1)
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # st = ''
#         # for i in self.marks:
#         #     st += str(i) + ", "
#         # return f"Студент => {self.name}: {st[:-2]}"
#         # st = ", ".join(map(str, self.marks))
#         # return f"Студент => {self.name}: {st}"
#         return f"Студент => {self.name}: {", ".join(map(str, self.marks))}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 1)
#
#     def get_file_name(self):
#         return self.name + ".json"  # 'Bodnya.json'
#
#     def dump_to_json(self):
#         data = {"name": self.name, "marks": self.marks}
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         st = "\n".join(map(str, self.students))
#         return f"Группа: {self.group}\n{st}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(gr1, gr2, index):
#         # st = gr1.remove_student(index)
#         # gr2.add_student(st)
#         gr2.add_student(gr1.remove_student(index))
#
#     def get_file_name(self):
#         return self.group.lower().replace(" ", "-") + ".json"
#
#     def dump_to_json(self):
#         data = [
#             {'name': student.name, 'marks': student.marks} for student in self.students
#         ]
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f, indent=2)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(4, 4)
# # print(st1)
# # print(st1.average_mark())
# # st1.dump_to_json()
# # st1.load_from_file()
# sts1 = [st1, st2]
# group1 = Group(sts1, "ГК Python")
# # print(group1)
# # print()
# group1.add_student(st3)
# # print(group1)
# # print()
# group1.remove_student(1)
# print(group1)
# print()
# sts2 = [st2]
# group2 = Group(sts2, "ГК Web")
# print(group2)
# print()
# Group.change_group(group1, group2, 0)
# print(group1)
# print(group2)
#
# group2.dump_to_json()
# group2.load_from_file()

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(type(response.text))
# # print(response.text)
# todos = json.loads(response.text)
# # print(todos)
# #
# todos_by_user = {}  # {1: 4, 2: 1}
# #
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]
#
# max_complete = top_users[0][1]
# print(max_complete)  # 12
#
# users = []  # ['5', '10']
# for user, num in top_users:
#     if num < max_complete:  # 11 < 12
#         break
#     users.append(str(user))
# print(users)
#
# max_users = " и ".join(users)
# print(max_users)
#
# print(f"Пользователи {max_users} выполнили {max_complete} задач")


import csv

# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#
# with open("data.csv") as f:
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=file_names)
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1
#
# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", 9, 15])
#     writer.writerow(["Саша", 5, 12])
#     writer.writerow(["Маша", 11, 17])
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#


# with open("data2.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#
# with open("sw_data.csv", "r") as f:
#     print(f.read())

# with open("student1.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": 6})
#     writer.writerow({"Имя": "Маша", "Возраст": 15})
#     writer.writerow({"Имя": "Вова", "Возраст": 14})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# Парсинг сайта

from bs4 import BeautifulSoup

import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)

#
# f = open("index.html").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find_all("div", {"class": "name"})
# row = soup.find("div", {"data-set": "salary"})
# row = soup.find("div", string="Alena")
# row = soup.find("div", string="Alena").parent.parent
# row = soup.find("div", string="Alena").find_parent(class_="row")

# row = soup.find("div", id="whois3").find_next_sibling()

# row = soup.find("div", id="whois3").find_previous_sibling()


# row = soup.find_all("div", {"data-set": "salary"})
# # print(row)
# for i in row:
#     get_salary(i.text)

import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     row = requests.get(url)
#     return row.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("div", id="intro").find("h1", class_="wp-block-heading").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# import csv
# import re
# import requests
# from bs4 import BeautifulSoup
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data["name"], data["url"], data["rating"]))
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def get_html(url):
#     row = requests.get(url)
#     return row.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all("li")
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a").get("href")
#         url = plugin.find("h3").find("a")["href"]
#         rating = plugin.find("span", class_="rating-count").text
#         r = refined(rating)
#
#         data = {"name": name, "url": url, "rating": r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# import csv
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     row = requests.get(url)
#     return row.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("li", class_="wp-block-post")
#     for el in elements:
#         name = el.find("h3").text
#         url = el.find("h3").find("a").get("href")
#         snippet = el.find("div", class_="entry-excerpt").text.strip()
#         active = el.find("span", class_="active-installs").text.strip()
#         tested = el.find("span", class_="tested-with").text.strip()
#         test = refine_cy(tested)
#         data = {
#             "name": name,
#             "url": url,
#             "snippet": snippet,
#             "active": active,
#             "test": test
#         }
#         write_csv(data)
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a", encoding="utf-8-sig") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data["name"], data["url"], data["snippet"], data["active"], data["test"]))
#
#
# def main():
#     for i in range(3, 23):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# #
# row = requests.get("https://ru.wordpress.org/plugins/browse/blocks")
# print(row.text)

# from parser import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]  # GET
#     url = parsed[1]  # / или /blog
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != "GET":
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found</h3>'
#     if code == 405:
#         return '<h1>405</h1><h3>Method Not Allowed</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_soket.bind(('127.0.0.1', 5000))  # 127.0.0.1:5000
#     server_soket.listen()
#
#     while True:
#         client_soket, addr = server_soket.accept()
#
#         request = client_soket.recv(1024)
#
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_soket.sendall(response)
#         client_soket.close()
#
#
# if __name__ == '__main__':
#     run()

from jinja2 import Template

# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a * 2 }} лет. Меня зовут {{ n.upper() }}.")
# msg = tm.render(n=name, a=age)
#
# print(msg)

# per = {'name': "Игорь", 'age': 28}
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p['name'] }}.")
# msg = tm.render(p=per)
#
# print(msg)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """
# <select>
# {% for c in cities %}
#     {% if c.id > 3 %}
#         <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#     {% elif c.city == 'Москва' %}
#         <option>{{ c['city'] }}</option>
#     {% else %}
#         {{ c['city'] }}
#     {% endif %}
# {% endfor %}
# </select>
# """
#
# # tm = Template(link)
# # msg = tm.render(cities=cities)
# #
# # print(msg)
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)

#
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """
# <select>
# {% for c in cities %}
#     {% if c.id > 3 %}
#         <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#     {% elif c.city == 'Москва' %}
#         <option>{{ c['city'] }}</option>
#     {% else %}
#         {{ c['city'] }}
#     {% endif %}
# {% endfor %}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)


# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'},
# ]
#
# link = """
# <ul>
#     {% for i in menu %}
#         {% if i.link == 'Главная' %}
#             <li><a href="{{ i['href'] }}" class="active">{{ i['link'] }}</a></li>
#         {% else %}
#             <li><a href="{{ i['href'] }}">{{ i['link'] }}</a></li>
#         {% endif %}
#     {% endfor %}
# </ul>
# """
#
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)

# cars = [
#     {"model": 'Audi', 'price': 23000},
#     {"model": 'Skoda', 'price': 17300},
#     {"model": 'Renault', 'price': 44300},
#     {"model": 'Wolksvagen', 'price': 21300}
# ]
# # cars = [3, 5, 7]
#
# # tpl = "{{ cs | sum(attribute='price') }}"
# # tpl = "{{ (cs | max(attribute='price')).model }}"
# tpl = "{{ (cs|min(attribute='price')).model }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# html = """
# {% macro set_input(name, value='', type='text', size=20) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}
#
# <p>{{ set_input('username') }}</p>
# <p>{{ set_input('email') }}</p>
# <p>{{ set_input('password', '', 'password') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# from jinja2 import Environment, FileSystemLoader
#
# persons = [
#     {"name": "Алексей"},
#     {"name": "Никита"},
#     {"name": "Виталий"},
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# msg = tm.render(users=persons, title="About Jinja")
#
# print(msg)

# import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("")
#
# con.close()

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     data TEXT
#     )""")
#     cur.execute("DROP TABLE users")

# import sqlite3
#
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT "+7 909 1234567",
#     age INTEGER CHECK(age > 0 AND age < 100),
#     email TEXT UNIQUE
#     )""")

    # # переименование таблицы
    # cur.execute("""
    # ALTER TABLE users
    # RENAME TO person_table;
    # """)

    # # добавление нового столбца
    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT;
    # """)

    # # Переименование столбца
    # cur.execute("""
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address;
    # """)

    # # удаление столбца
    # cur.execute("""
    #     ALTER TABLE person_table
    #     DROP COLUMN home_address;
    #     """)
# import sqlite3
#
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS users(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# phone BLOB NOT NULL DEFAULT "+7 909 1234567",
# age INTEGER CHECK(age > 0 AND age < 100),
# email TEXT UNIQUE
# )""")

# # переименование таблицы
# cur.execute("""
# ALTER TABLE users
# RENAME TO person_table;
# """)

# # добавление нового столбца
# cur.execute("""
# ALTER TABLE person_table
# ADD COLUMN address TEXT;
# """)

# # Переименование столбца
# cur.execute("""
# ALTER TABLE person_table
# RENAME COLUMN address TO home_address;
# """)

# # удаление столбца
# cur.execute("""
#     ALTER TABLE person_table
#     DROP COLUMN home_address;
#     """)


# import sqlite3
#
# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM T1
#     LIMIT 2, 5
#     """)

    # for res in cur:
    #     print(res)
#     res = cur.fetchall()
#     print(res)
#
#     res2 = cur.fetchmany(2)
#     print(res2)
#     #
#     res1 = cur.fetchone()
#     print(res1)
#

import sqlite3

# car_list = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]

with sqlite3.connect("car.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )""")

cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")
# cur.executescript("""
# DELETE FROM cars WHERE model LIKE 'B%';
# UPDATE cars SET price = price + 100;
# """)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", car_list)

# for car in car_list:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)



# con.commit()
# con.close()
# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()


# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_id = cur.lastrowid
#     buy_id = 2
#     cur.execute("INSERT INTO cost  VALUES('Илья', ?, ?)", (last_id, buy_id))


# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     """)
#
#     cur.execute("SELECT model, price FROM cars")
#
#     # rows = cur.fetchall()
#     # print(rows)
#
#     # rows2 = cur.fetchone()
#     # print(rows2)
#     #
#     # rows3 = cur.fetchmany(5)
#     # print(rows3)
#
#     for res in cur:
#         print(res['model'], res['price'])

# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );""")
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)

# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)


# with sqlite3.connect("cars_db.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()

#         cur.executescript(sql)

