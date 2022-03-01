# First Trial
# 시간초과

T = int(input())

def fib(n):
    if n == 0:
        global cnt0
        cnt0 += 1
        return 0
    elif n == 1:
        global cnt1
        cnt1 += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

for _ in range(T):
    cnt0 = 0
    cnt1 = 0
    fib(int(input()))
    print(cnt0, cnt1)

# Second Trial
# Error (memo call 할 수 없는 구조)

T = int(input())
memo = {}

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        global memo
        if n not in memo:
            global cnt0
            global cnt1
            if n - 1 == 0 or n - 2 == 0:
                cnt0 += 1
            if n - 1 == 1 or n - 2 == 1:
                cnt1 += 1
            memo[n] = [fib(n - 1) + fib(n - 2), cnt0 + memo[n - 1][1] + memo[n - 2][1], cnt1+ memo[n - 1][2] + memo[n - 2][2]]
        return memo[n][0]

for _ in range(T):
    cnt0 = 0
    cnt1 = 0

    n = int(input())
    fib(n)
    print(memo[n][1], memo[n][1])


# Third Solution
# Bottom-up
# Solved (메모리 30860 KB, 시간 72 ms)

T = int(input())

for _ in range(T):
    n = int(input())
    fib = [0] * (n + 1)
    cnt0 = [0] * (n + 1)
    cnt1 = [0] * (n + 1)
    for i in range(n + 1):
        if i == 0:
            cnt0[i] = 1
            fib[i] = 0
        elif i == 1:
            cnt1[i] = 1
            fib[i] = 1
        else:
            fib[i] = fib[i - 1] + fib[i - 2]
            cnt0[i] = cnt0[i - 1] + cnt0[i - 2]
            cnt1[i] = cnt1[i - 1] + cnt1[i - 2]
    print(cnt0[n], cnt1[n])

# =========================
# Other's solution
# 피보나치 수의 생성 규칙과 동일한 방식으로 0과 1이 출현
# 값: 1 2 3 4 5 6 7 ...
# 0: 0 1 1 2 3 5 8 ...
# 1: 1 1 2 3 5 8 13 ...
# Solved (메모리 30864 KB, 시간 76 ms)

cnt0 = [1, 0]
cnt1 = [0, 1]

T = int(input())

for _ in range(T):
    n = int(input())
    if n == 0:
        # print(cnt0[0], cnt1[0])
        print("1 0")
    elif n == 0:
        # print(cnt0[1], cnt1[1])
        print("0 1")
    else:
        for i in range(2, n + 1):
            cnt0.append(cnt0[i - 1] + cnt0[i - 2])
            cnt1.append(cnt1[i - 1] + cnt1[i - 2])
        print(cnt0.pop(), cnt1.pop())
        cnt0 = [1, 0]
        cnt1 = [0, 1]