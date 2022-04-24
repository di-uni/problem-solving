#  First Trial
# Solved (메모리 30840 KB, 시간 68 ms)

N = int(input())
P = sorted(list(map(int, input().split())))

prefixSum, total = 0, 0

for p in P:
    prefixSum += p
    total += prefixSum

print(total)