# =========================
# Other's solution
# Solved (메모리 30864 KB, 시간 68 ms)

import sys
input = sys.stdin.readline

N = int(input())
dp = [0,1,2,4]

for _ in range(N):
    t = int(input())
    i = len(dp)
    while i <= t:
        dp.append(dp[i-3] + dp[i-2] + dp[i-1])
        i += 1
    print(dp[t])