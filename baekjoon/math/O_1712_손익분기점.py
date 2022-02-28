# a + b * n <= c * n
# n * (c - b) >= a
# n >= a / (c - b)


# First Trial

import math
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
    exit(0)
if A % (C - B) == 0:
    print(int(A / (C - B)) + 1)
else:
    print(math.ceil(A / (C - B)))


# Second Trial referred to other's solution
# 몫(//)을 이용하면 깔끔한 정리 가능

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(A // (C - B) + 1)