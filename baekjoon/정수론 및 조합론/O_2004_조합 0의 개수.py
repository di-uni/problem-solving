# First Trial
# 메모리 초과

import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
dp = {}
cnt = 0

def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n not in dp:
        dp[n] = n * factorial(n - 1)
    return dp[n]

result = factorial(N) // (factorial(N - K) * factorial(K))

while result >= 10:
    if result % 10 == 0:
        cnt += 1
        result //= 10
    else:
        break
    
print(cnt)


# Second Trial
# Solved (메모리 30848 KB, 시간 72 ms)

N, M = map(int, input().split())

cnt5 = 0
cnt2 = 0

temp = N
while temp >= 5:
    cnt5 += temp // 5
    temp //= 5

temp = N
while temp >= 2:
    cnt2 += temp // 2
    temp //= 2

temp = N - M
while temp >= 5:
    cnt5 -= temp // 5
    temp //= 5

temp = N - M
while temp >= 2:
    cnt2 -= temp // 2
    temp //= 2

temp = M
while temp >= 5:
    cnt5 -= temp // 5
    temp //= 5

temp = M
while temp >= 2:
    cnt2 -= temp // 2
    temp //= 2

print(min(cnt2, cnt5))


# Third Trial
# Reduce reputation
# Solved (메모리 30840 KB, 시간 68 ms)

N, M = map(int, input().split())

cnt5 = 0
cnt2 = 0

def count(n, plusOrMinus):
    global cnt2, cnt5
    division = [2, 5]
    for i in range(2):
        temp = n
        while temp >= division[i]:
            if i == 0:
                if plusOrMinus:
                    cnt2 += temp // division[i]
                else:
                    cnt2 -= temp // division[i]
            else:
                if plusOrMinus:
                    cnt5 += temp // division[i]
                else:
                    cnt5 -= temp // division[i]
            temp //= division[i]

count(N, True)
count(N-M, False)
count(M, False)

print(min(cnt2, cnt5))



# ===================================
# Other's solution
# 5, 2 세는 함수를 분리
# Solved (메모리 30840 KB, 시간 72 ms)

N, M = map(int, input().split())

def five_count(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt 
   
def two_count(n):
    cnt = 0
    while n != 0:
        n //= 2
        cnt += n
    return cnt 



print(min(two_count(N) - two_count(N-M) - two_count(M)
    , five_count(N) - five_count(N-M) - five_count(M)))