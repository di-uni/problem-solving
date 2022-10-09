# # First Trial
# # Wrong Answer

N = int(input())
virus = set([1])

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a in virus:
        virus.add(b)
    elif b in virus:
        virus.add(a)

print(len(virus) - 1)



# 2022.10.09
# Second Trial
# Solved (메모리 32412 KB, 시간 92 ms)

from collections import defaultdict

N = int(input())
M = int(input())
graph = defaultdict(list)
visited = [False] * (N + 1)

def dfs(M, graph, visited):
    ans = 0
    if M == 0: return ans

    for _ in range(M):
        first, second = map(int, input().split(" "))
        graph[first].append(second)
        graph[second].append(first)
        
    stack = set([1])
    visited[0] = True

    while stack:
        node = stack.pop()
        # print(node, stack)
        visited[node] = True
        for next_node in graph[node]:
            if not visited[next_node] and next_node not in stack:
                stack.add(next_node)
                ans += 1
    return ans

print(dfs(M, graph, visited))

# =============================================
# Other's Solution
# using DFS, visited에 0/1로 표시
# Solved (메모리 39572 KB, 시간 124 ms)

n = int(input())		# 컴퓨터의 수
m = int(input())		# 연결된 컴퓨터 쌍의 수

# 인접리스트 graph 선언 및 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):							# 연결된 컴퓨터 쌍의 수만큼 반복
    x, y = map(int, input().split())		
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)	# 방문처리 : 방문한 컴퓨터 수를 출력해야하므로 visited 에 True/False가 아닌 0/1로 처리

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
    return True

dfs(graph, 1, visited)
print(sum(visited)-1)	# 방문한 컴퓨터 개수 - 1번 컴퓨터