student = {}
s = 0
n = int(input("Кол-во студентов: "))
for i in range(n):
    name = input(str(i + 1) + "-й студент:")
    point = int(input("Балл: "))
    student[name] = point
    s += point

average = s / n

print("Средний бал: ", round(average), ".Студенты с балом выше среднего: ", sep="")

for i in student:
    if student[i] > average:
        print(i)