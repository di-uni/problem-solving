# First Trial
# Solved (메모리 31304 KB, 시간 68 ms)

import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
dp = {}

def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n not in dp:
        dp[n] = n * factorial(n - 1)
    return dp[n]

print((factorial(N) // (factorial(N - K) * factorial(K))) % 10007)

# ===================================
# Other's solution 
# 파스칼의 삼각형 사용
# Solved (메모리 48112 KB, 시간 272 ms)

import sys
N, K = map(int, sys.stdin.readline().split())
dp = [[1]*(i + 1) for i in range(N + 1)]

for i in range(2, N + 1):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007
    
print(dp[N][K])
