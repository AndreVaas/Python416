a = [int(input("-> ")) for i in range(int(input("n = ")))]
print(a)
minusSum = 0
for num in a:
    if num < 0:
        minusSum += num
print("Сумма отрицательных элементов:", + minusSum)