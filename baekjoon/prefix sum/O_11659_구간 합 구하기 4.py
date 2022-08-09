# First Trial
# Solved (메모리 40596 KB, 시간 284 ms)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = []
temp = 0

for n in nums:
    temp += n
    sums.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(sums[j - 1])
    else:
        print(sums[j - 1] - sums[i - 2])



# =============================================
# Other's Solution
# padding 이용
# Solved (메모리 40596 KB, 시간 264 ms)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0] * (N + 1)

for i in range(N):
    sums[i + 1] = sums[i] + nums[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(sums[j] - sums[i - 1])
