# First Trial
# Solved (메모리 48524 KB, 시간 268 ms)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}

for i in range(1, N + 1):
    mon = input().rstrip()
    dict[mon] = i
    dict[i] = mon

for _ in range(M):
    cmd = input().rstrip()
    if cmd.isdigit():
        print(dict[int(cmd)])
    else:
        print(dict[cmd])