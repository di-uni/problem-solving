import math

A, B, V = map(int, input().split())

# A * n - B * (n - 1) > V
# n * (A - B) > V - B
# n > (V - B) / (A - B)

time = (V - B) / (A - B)
if (V - B) % (A - B) == 0:
    print(int(time))
else:
    print(math.ceil(time))
