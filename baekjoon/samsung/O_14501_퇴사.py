# First Trial
# Solved (메모리 30840 KB, 시간 72 ms)

N = int(input())
T = [0]
P = [0]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

def choice(i, val, j):
    if i + T[i] == N + 1:
        if i < N:
            return max(val + P[i], choice(i + 1, val, i))
        else:
            return val + P[i]
    if i + T[i] > N + 1:
        if i < N:
            return max(val, choice(i + 1, val, i))
        return val
    if T[i] == 1:
        return choice(i + T[i], val + P[i], i)
    return max(choice(i + T[i], val + P[i], i), choice(i + 1, val, i))

print(choice(1, 0, 0))




# ======================================
# Other's solution 
# dp 사용
# Solved (메모리 30840 KB, 시간 68 ms)

N = int(input())
T = []
P = []
dp = [0] * (N + 1)

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N - 1, -1, -1):
    if T[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

print(dp[0])