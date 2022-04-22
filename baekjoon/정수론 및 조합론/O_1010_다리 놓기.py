# First Trial
# Solved (메모리 30840 KB, 시간 100 ms)

import sys
sys.setrecursionlimit(10**6)

dp = {}

def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n not in dp:
        dp[n] = n * factorial(n - 1)
    return dp[n]

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print((factorial(M) // (factorial(M - N) * factorial(N))))