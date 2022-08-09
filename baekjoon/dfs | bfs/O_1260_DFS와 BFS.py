# First Trial referred to Other's Solution
# Solved (메모리 32468 KB, 시간 108 ms)

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(i):
    print(i, end=' ')
    visited[i] = True
    for x in graph[i]:
        if not visited[x]:
            dfs(x)
            visited[x] = True

def bfs(i):
    queue = deque([i])
    visited[i] = True

    while queue:
        val = queue.popleft()
        print(val, end=' ')

        for x in graph[val]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True

dfs(V)
visited = [False] * (N + 1)

print()
bfs(V)