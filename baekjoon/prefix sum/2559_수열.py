# First Trial
# Solved (메모리 39724 KB, 시간 152 ms)

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

k_list = deque([])
sum_val = 0
max_val = 0

for i in range(K):
    k_list.append(nums[i])
    sum_val += nums[i]
max_val = sum_val
# print(nums[i], max_val)

for i in range(K, len(nums)):
    sum_val -= k_list.popleft()
    k_list.append(nums[i])
    sum_val += nums[i]
    max_val = max(max_val, sum_val)
    # print(k_list, max_val)

print(max_val)


# =============================================
# Other's Solution
# 메모리 좀 더 효율적으로 (k_list X)
# Solved (메모리 39572 KB, 시간 124 ms)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

part_sum = sum(nums[:K])
max_val = part_sum

for i in range(K, N):
    part_sum += nums[i] - nums[i - K]
    max_val = max(part_sum, max_val)

print(max_val)
