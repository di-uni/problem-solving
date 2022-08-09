# # First Trial
# # Wrong Answer

# N = int(input())
# virus = set([1])

# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     if a in virus:
#         virus.add(b)
#     elif b in virus:
#         virus.add(a)

# print(len(virus) - 1)


# =============================================
# Other's Solution
# using DFS
# Solved (메모리 39572 KB, 시간 124 ms)


import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict

N = int(input())
graph = defaultdict(list)

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [False] * (N + 1)

def dfs(start):
    global cnt
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)