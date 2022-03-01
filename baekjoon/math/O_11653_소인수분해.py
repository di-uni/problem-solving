# for문 돌려서 계속 나누기
# 소수임을 확인하기
# --------------------
# N보다 작은 소수 구하기
# 그 소수로 계속 나눠보기

# =========================
#  First Trial
#  시간 초과

import math, sys

N = int(sys.stdin.readline().rstrip())
prime = []
prime_factor = []

if N == 1:
    exit(0)

for i in range(2, round(N / 2)):
    j = 2
    isPrime = 1
    while j * j <= i:
        if i % j == 0:
            isPrime = 0
        j += 1
    if isPrime == 1:
        prime.append(i)

Ncopy = N
for p in prime:
    while Ncopy % p == 0:
        print(p)
        prime_factor.append(p)
        Ncopy /= p

if len(prime_factor) == 0:
    print(N)

# Second Trial (에라토스테네스의 체)
# 메모리 초과

N = int(input())

# get the prime number
prime = {2} | {i for i in range(3, N + 1) if i % 2 == 1}
for odd in range(3, int(N ** 0.5) + 1, 2):
    if odd in prime:
        prime -= {i for i in range(2 * odd, N + 1, odd)}

if N in prime:
    print(N)
else:
    for p in prime:
        while N % p == 0:
            N /= p
            print(p)
        if N == 1:
            break


# Third Trial
# 시간 초과

N = int(input())

while N % 2 == 0:
    N /= 2
    print(2)

max_num = int(N) + 1
for i in range(3, max_num):
    isPrime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        while N % i == 0:
            N /= i
            print(i)
    if N == 1:
        break

# ================================
# Forth Trial
# 2 ~ n의 제곱근 범위의 소수를 구해서 나눠준다. 이후에 남은 수는 결국 소수임!
# Solved (메모리 30864 KB, 시간 84 ms)

N = int(input())

while N % 2 == 0:
    N /= 2
    print(2)

max_num = int(N ** 0.5) + 1
for i in range(3, max_num):
    isPrime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        while N % i == 0:
            N //= i
            print(i)
    if N == 1:
        break
if N != 1:
    print(int(N))   # 이 수는 무조건 소수!

# ========================================
# Other's solution
# 에라토스테네스의 체의 원리
# 나누는 값을 계속 증가시켜주면서 나누어떨어지는지 확인하면 된다.
# Solved (메모리 30864 KB, 시간 1460 ms)

N = int(input())
m = 2
while N != 1:
    if N % m == 0:
        print(m)
        N //= m
    else:
        m += 1