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