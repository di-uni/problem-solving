# First Trial
# 시간 초과

import sys
sys.setrecursionlimit(10**6)

N = int(input())
cnt = 0

def dp(i):
    # print(i)
    if i == N:
        global cnt
        cnt += 1
        return
    if i + 2 <= N:
        dp(i + 2)
    dp(i + 1)

dp(0)

print(cnt % 15746)


# Second Trial referred to other's solution
# 메모리 초과

import sys
sys.setrecursionlimit(10**6)

N = int(input())
cnt = 0
memo = {}

def dp(i):
    if i == 0:
        return 1
    if i == 1:
        return 1
    if i not in memo:
        memo[i] = dp(i - 1) + dp(i - 2)
    return memo[i]

print(dp(N) % 15746)



# ===========================================
# Other's Solution
# Solved (메모리 69396 KB, 시간 388 ms)

import sys
sys.setrecursionlimit(10**6)

N = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for k in range(3, N + 1):
    dp[k] = (dp[k-1] + dp[k-2]) % 15746
print(dp[N])