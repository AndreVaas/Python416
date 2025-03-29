import random
mas = [random.randint(0, 100) for i in range(10)]
print(mas)
a = mas.copy()
a.sort()
n = a[0]
print("Min:", n)
value = n
if value in a:
    ind = mas.index(value, 0, 10)
    print("Index min:", ind)
    mas[:ind] = []
print(mas)