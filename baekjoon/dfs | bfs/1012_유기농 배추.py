# First Trial
# Solved (메모리 33220 KB, 시간 84 ms)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N:
        return False
    if ground[y][x] == 1:
        ground[y][x] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1
    
    result = 0
    for i in range(M):
        for j in range(N):
            if dfs(i, j) == True:
                result += 1
    
    print(result)


# ===================================
# Other's solution
# use bfs
# Solved (메모리 32440 KB, 시간 100 ms)

import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())

def bfs(graph, a, b):
    queue = deque([(a, b)])
    graph[a][b] = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))
    return

for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for b in range(M):
        for a in range(N):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    
    print(cnt)