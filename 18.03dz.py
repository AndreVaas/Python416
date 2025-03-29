def finding_negative(n):
    if not n:
        return 0
    c = 0
    if n[0] < 0:
        c += 1
    return c + finding_negative(n[1:])


numbers = [-2, 3, 8, -11, -4, 6]


print(f'n = {finding_negative(numbers)}')