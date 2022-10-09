# First Trial
# 메모리 초과

import sys
sys.setrecursionlimit(10**6)

N = int(input())
cnt = 0

def dp(x, cnt):
    if x == 1:
        return cnt
    if x % 3 == 0 and x % 2 == 0:
        return min(dp(x - 1, cnt + 1), dp(x // 3, cnt + 1), dp(x // 2, cnt + 1))
    elif x % 3 != 0 and x % 2 == 0:
        return min(dp(x - 1, cnt + 1), dp(x // 2, cnt + 1))
    elif x % 3 == 0 and x % 2 != 0:
        return min(dp(x - 1, cnt + 1), dp(x // 3, cnt + 1))
    else:
        return dp(x - 1, cnt + 1)

print(dp(N, 0))


# 2022.10.09
# Second Trial
# 시간 초과

from heapq import heappush, heappop

N = int(input())
heap = []
dp = set([])
heappush(heap, (0, N))

while heap:
    cnt, val = heappop(heap)
    dp.add((cnt, val))
    if val == 1:
        print(cnt)
        break
    if val % 3 == 0:
        if (cnt + 1, val // 3) not in dp:
            heappush(heap, (cnt + 1, val // 3))
    if val % 2 == 0:
        if (cnt + 1, val // 2) not in dp:
            heappush(heap, (cnt + 1, val // 2))
    if (cnt + 1, val - 1) not in dp:
        heappush(heap, (cnt + 1, val - 1))


# =============================================
# Other's Solution
# using dp
# Solved (메모리 38652 KB, 시간 652 ms)

N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    
# print(dp)
print(dp[N])