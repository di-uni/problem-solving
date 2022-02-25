# for문 돌려서 계속 나누기
# 소수임을 확인하기
# --------------------
# N보다 작은 소수 구하기
# 그 소수로 계속 나눠보기

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

