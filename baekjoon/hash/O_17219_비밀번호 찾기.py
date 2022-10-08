# First Solution
# Bottom-up
# Solved (메모리 49788 KB, 시간 264 ms)

import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
sitePassword = {}

for _ in range(N):
    site, password = input().strip().split(" ")
    sitePassword[site] = password

for _ in range(M):
    print(sitePassword[input().strip()])