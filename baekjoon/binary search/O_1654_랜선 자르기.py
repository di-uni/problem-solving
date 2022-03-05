# First Trial
# 시간 초과

import sys

K, N = map(int, input().split())
cables = []

for k in range(K):
    cables.append(int(sys.stdin.readline().rstrip()))
cables.sort()

for i in range(cables[-2], 0, -1):
    cnt = 0
    for cable in cables:
        cnt += cable // i 
    if cnt >= N:
        print(i)
        break


# Second Trial
# Using binary search
# Solved (메모리 30864 KB, 시간 128 ms)

import sys

K, N = map(int, input().split())
cables = []
ans = []

for k in range(K):
    cables.append(int(sys.stdin.readline().rstrip()))

left, right = 1, max(cables)
while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for cable in cables:
        cnt += cable // mid
    if cnt >= N:
        ans.append(mid)
        left = mid + 1
    else:
        right = mid - 1

print(max(ans))


# =======================================================
# Other's solution
# cables 간단히 정리, ans에 따로 append하지 않고 max값 바로 구하기
# Solved (메모리 30864 KB, 시간 116 ms)

import sys

K, N = map(int, input().split())
cables = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

left, right = 1, max(cables)
while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for cable in cables:
        cnt += cable // mid
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)