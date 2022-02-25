# First Trial

T = int(input())
sum_dict = {}

def sum_peole(k, n):
    if k == 0:
        return n
    ans = 0
    if (k, n) in sum_dict:
        return sum_dict[(k, n)]
    if (k, n) not in sum_dict:
        for i in range(1, n + 1):
            ans += sum_peole(k - 1, i)
        sum_dict[(k, n)] = ans
        return ans

for t in range(T):
    k = int(input())
    n = int(input())
    print(sum_peole(k, n))

# Second Trial referred to other's solution
# more optimized

T = int(input())
sum_dict = {}

def sum_peole(k, n):
    if k == 0:
        return n
    if n == 0:
        return 0
    if (k, n) not in sum_dict:
        sum_dict[(k, n)] = sum_peole(k - 1, n) + sum_peole(k, n - 1)
    return sum_dict[(k, n)]

for t in range(T):
    k = int(input())
    n = int(input())
    print(sum_peole(k, n))

# Third Trial referred to other's solution
# Bottom-up

T = int(input())

for t in range(T):
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num + 1)]
    for k in range(floor):
        for n in range(1, num):
            f0[n] += f0[n-1]
    print(f0[-1])

