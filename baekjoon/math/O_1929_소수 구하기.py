# First Trial
# Solved

M, N = map(int, input().split())
num = [0] * (N + 1)

for i in range(2, N):
    if num[i] == 0:
        j = 2
        while j * i < N + 1:
            num[j * i] = 1
            j += 1

for i in range(max(2, M), N + 1):
    if num[i] == 0:
        print(i)

# =========================
# Other's solution
# 0,1 대신 True, False를 list에 넣음
# n의 제곱근까지만 검사해도 된다는 점

m, n = map(int, input().split())

def isPrime(m, n):
    n += 1
    prime = [True] * n
    for i in range(2, int(n**0.5) + 1): # n의 제곱근까지만 검사
        if prime[i]:
            for j in range(2 * i, n, i):
                prime[j] = False

    for i in range(max(2, m), n):
        if prime[i] == True:
            print(i)
            
isPrime(m, n)