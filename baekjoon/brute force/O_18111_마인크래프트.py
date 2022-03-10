# First Trial
# Solved (메모리 30864 KB, 시간 180 ms)

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
mine = {}
time, mean = float("inf"), 0

for x in range(N):
    for y in map(int, input().split()):
        if y not in mine:
            mine[y] = 0
        mine[y] += 1

for temp_mean in range(min(mine.keys()), max(mine.keys()) + 1):
    temp_time, add, use = 0, 0, 0
    for block in mine.keys():
        if block > temp_mean:
            temp_time += (block - temp_mean) * mine[block] * 2
            add += (block - temp_mean) * mine[block]
        elif block < temp_mean:
            temp_time += (temp_mean - block) * mine[block]
            use += (temp_mean - block) * mine[block]
    if use <= (add + B):
        time = min(time, temp_time)
        if time == temp_time:
            mean = temp_mean

print(time, mean)

# ==========================================================
# Other's solution
# O(MN), brute force
# 시간 초과 (흠?)

import sys

N, M, B = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
height = 0
ans = float("inf")

for i in range(257):
    add, use = 0, 0
    for j in range(N):
        for k in range(M):
            if table[j][k] < i:
                add += (i - table[j][k])
            else:
                use += (table[j][k] - 1)
    if add + B < use:
        continue
    time = 2 * add + use
    if time <= ans:
        ans = time
        height = i
print(ans, height)