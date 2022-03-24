# First Trial
# Solved (메모리 30864 KB, 시간 76 ms)

N, M = map(int, input().split())
s = []
visited = [False] * (N + 1)

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))

    for i in range(1, N + 1):
        if not visited[i] and (len(s) == 0 or i > max(s)):
            s.append(i)
            visited[i] = True
            dfs()
            visited[i] = False
            s.pop()

dfs()


# =========================
# Other's solution
# add 'start' variable
# Solved (메모리 30864 KB, 시간 72 ms)

N, M = map(int, input().split())
s = []
visited = [False] * (N + 1)

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))

    for i in range(start, N + 1):
        if not visited[i]:
            s.append(i)
            visited[i] = True
            dfs(i + 1)
            visited[i] = False
            s.pop()

dfs(1)