# First Trial
# Solved (메모리 31148 KB, 시간 992 ms)

memo = {}

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if (a, b, c) not in memo:
        if a < b and b < c:
            memo[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            memo[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return memo[(a, b, c)]

while True:
    a, b, c = list(map(int, input().split()))
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")


# ======================================
# Other's solution
# dp 3d array 사용(메모리, 속도가 dictionary보다 압도적)
# Solved (메모리 30864 KB, 시간 112 ms)

import sys

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if not dp[a][b][c]:
        if a < b and b < c:
            dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
# 0 ~ 20까지이므로

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")