# First Trial
# 시간 초과

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
ans = []

# left, right = min(trees), max(trees) - 1
left, right = 0, max(trees) - 1
# print(left, right)
while left <= right:
    mid = (left + right) // 2
    val = 0
    for t in trees:
        if t > mid:
            val += t - mid
    # print(left, right, mid, val)
    if val == M:
        print(mid)
        break
    elif val < M:
        right = mid - 1
    else:
        left = mid + 1
        ans.append(mid)
else:
    print(max(ans))


# Second Trial referred to other's solution
# list(=ans) 제외
# Solved (메모리 153536 KB, 시간 3316 ms)

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(trees) - 1
while left <= right:
    mid = (left + right) // 2
    val = [t-mid if t > mid else 0 for t in trees]
    total_val = sum(val)
    if total_val >= M:
        left = mid + 1
    else:
        right = mid - 1
print(right)