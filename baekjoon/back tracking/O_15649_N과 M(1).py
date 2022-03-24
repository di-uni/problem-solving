# First Trial
# Solved (메모리 30864 KB, 시간 240 ms)

import itertools

N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]

nPr = itertools.permutations(nums, M)

for items in nPr:
    for item in items:
        print(item, end=' ')
    print()



# =========================
# Other's solution
# Using Back-tracking (a type of dfs)
# Solved (메모리 30864 KB, 시간 212 ms)

N, M = map(int, input().split())
visited = [False] * (N + 1)
s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))

    for i in range(1, N + 1):
        if not visited[i]:
            s.append(i)
            visited[i] = True
            dfs()
            visited[i] = False
            s.pop()

dfs()