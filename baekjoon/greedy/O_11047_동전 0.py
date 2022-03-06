# First Trial
# 시간 초과

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

value = K
cnt = 0

for i in range(N - 1, -1, -1):
    if K < coins[i]:
        continue
    while value - coins[i] >= 0:
        value -= coins[i]
        cnt += 1
    if value == 0:
        print(cnt)
        break


# ======================================
# Other's solution
# 값을 빼주는게 아닌 나눠주기
# Solved (메모리 30864 KB, 시간 76 ms)

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

value = K
cnt = 0

for i in range(N - 1, -1, -1):
    if K < coins[i]:
        continue
    cnt += value // coins[i]
    value %= coins[i]
    if value == 0:
        print(cnt)
        break