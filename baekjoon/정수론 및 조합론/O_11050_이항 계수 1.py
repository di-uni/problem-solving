# First Trial
# Solved (메모리 30864 KB, 시간 68 ms)

N, K = map(int, input().split())
ans = 1

for i in range(K):
    ans *= (N - i)
    ans /= (K - i)

print(round(ans))


# ===================================
# Other's solution (1)
# factorial 재귀문 사용 (Top-down)
# Solved (메모리 30864 KB, 시간 72 ms)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

N, K = map(int, input().split())
print(factorial(N) // (factorial(K) * factorial(N - K)))


# Other's solution (2)
# factorial 반목문 사용 (Bottom-up)
# Solved (메모리 30864 KB, 시간 68 ms)

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

N, K = map(int, input().split())
print(factorial(N) // (factorial(K) * factorial(N - K)))
