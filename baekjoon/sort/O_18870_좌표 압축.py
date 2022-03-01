# First Trial
# 시간 초과

N = int(input())
nums = list(map(int, input().split()))
ans = ""

for n in nums:
    temp = 0
    for i in range(N):
        if n > nums[i]:
            temp += 1
    ans += str(temp) + " "

print(ans.rstrip())

# Second Trial referred to other's solution
# Solved (메모리 148208 KB, 시간 2084 ms)

N = int(input())
nums = list(map(int, input().split()))
ans = ""

sorted_nums = sorted(nums)
ranks = {}
i = 0
for n in sorted_nums:
    if n not in ranks:
        ranks[n] = i
        i += 1

for n in nums:
    ans += str(ranks[n]) + " "

print(ans.rstrip())


# =========================
# Other's solution
# Solved (메모리 144088 KB, 시간 2236 ms)
# set 사용, dict 숏코딩

import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

ranks = list(sorted(set(nums)))
ranks_dict = { ranks[i]:i for i in range(len(ranks)) }

for n in nums:
    print(ranks_dict[n], end=' ')

