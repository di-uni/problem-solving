# First Trial
# 시간 초과

T = int(input())
prime = [True] * 10001
prime[1] = False
max_num = 2

for _ in range(T):
    n = int(input())
    n_prime = []
    gold = [0, float("inf")]
    if max_num < int(n ** 0.5) + 1:
        for i in range(max_num, int(n ** 0.5) + 1):
            for j in range(2*i, 10000, i):
                prime[j] = False
        max_num = int(n ** 0.5) + 1
    # print(prime[:20])
    for i in range(2, n):
        if prime[i]:
            n_prime.append(i)
    for p in n_prime:
        if n - p in n_prime:
            if gold[1] - gold[0] > n - p - p:
                gold = [p, n-p]
            n_prime.remove(n-p)
    print(gold[0], gold[1])


# Second Trial
# Solved (메모리 30864 KB, 시간 3140ms)

T = int(input())
prime = [True] * 10001
prime[1] = False
max_num = 2

for _ in range(T):
    n = int(input())
    gold = [0, float("inf")]
    if max_num < int(n ** 0.5) + 1:
        for i in range(max_num, int(n ** 0.5) + 1):
            for j in range(2*i, 10000, i):
                prime[j] = False
        max_num = int(n ** 0.5) + 1
    # print(prime[:20])
    for p in range(2, n):
        if prime[p] and prime[n - p] and p <= n - p:
            if gold[1] - gold[0] > n - p - p:
                gold = [p, n-p]
    print(gold[0], gold[1])


# =========================
# Other's solution
# Solved (메모리 31376 KB, 시간 560ms)

max_n = 10000
nums = {2} | {x for x in range(3, max_n + 1) if x % 2 == 1}
# nums: 2와 홀수로 이루어진 집합

for odd in range(3, int(max_n ** 0.5) + 1, 2):
    nums -= {i for i in range(2 * odd, max_n + 1, odd) if i in nums}
    # 홀수의 배수로 이루어진 집합을 빼준다

T = int(input())
for _ in range(T):
    n = int(input())
    for p in range(n//2, 1, -1):    # 차이가 적은 두 수를 구하기 위해서 큰 수부터 확인
        if (p in nums) and (n - p in nums):
            print(p, n-p)
            break
