num = int(input("Введите пятизначное число: "))
a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
num = num // 10
d = num % 10
num = num // 10
e = num % 10

product_of_numbers = a * b * c * d * e
arithmetic_mean = (a + b + c + d + e) / 5
print("Произведение чисел:", product_of_numbers)
print("Среднее арифметическое:", arithmetic_mean)
