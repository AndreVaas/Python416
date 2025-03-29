import random


def generate_tuple(a, b):
    return tuple(random.randint(a, b) for i in range(10))


tpl1 = generate_tuple(0, 5)
tpl2 = generate_tuple(-5, 0)


tpl3 = tpl1 + tpl2

zero_count = tpl3.count(0)

print(tpl1)
print(tpl2)
print(tpl3)
print("0 =", zero_count)