a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
b = []
for i in a:
    num = 0
    for n in a:
        if i == n:
            num += 1
    if num == 1:
        b.append(i)

print(a)
print()
print(b)