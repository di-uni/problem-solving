import math
a, b, c = map(int, input().split())

# a + b * n <= c * n
# n * (c - b) >= a
# n >= a / (c - b)
print(a / (c - b))
if c - b == 0:
    print(-1)
if a % (c - b) == 0:
    print(a / (c - b) + 1)
elif a / (c - b) < 0:
    print(-1)
else:
    print(math.ceil(a / (c - b)))