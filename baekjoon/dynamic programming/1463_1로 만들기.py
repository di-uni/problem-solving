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