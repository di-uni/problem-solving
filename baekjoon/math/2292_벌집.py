n = int(input()) - 1
d = 1
i = 1

while n > 0:
    n -= 6 * i
    i += 1
    d += 1
print(d)