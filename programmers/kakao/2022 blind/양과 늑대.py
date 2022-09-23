# First Trial
# Test Passed

from collections import defaultdict
def solution(info, edges):
    answer = 0
    
    next_nodes = defaultdict(list)
    for i, j in edges:
        next_nodes[i].append(j)

    def dfs(sheep, wolf, cur, path):
        wolf += info[cur]
        sheep += info[cur] ^ 1
            
        if sheep <= wolf:
            return 0
        
        maxSheep = sheep
        
        for p in path:
            for n in next_nodes[p]:
                if n not in path:
                    path.append(n)
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n, path))
                    path.pop()
        # print(maxSheep)
        return maxSheep
    
    answer = dfs(0, 0, 0, [0])
    return answer


# Second Trial
# Test Failed

from collections import defaultdict

def solution(info, edges):
    answer = 0
    graph = defaultdict(list)
    sheep, wolves = 0, 0
    visited = [False] * len(info)
    
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    stack = [0]
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            sheep += info[curr] ^ 1
            wolves += info[curr]
            visited[curr] = True
        if sheep > wolves:
            answer = max(answer, sheep)
            for edge in graph[curr]:
                if edge not in stack:
                    stack.append(edge)
        else:
            if info[curr]:
                wolves -= info[curr]
                visited[curr] = False
        print(stack, sheep, wolves)
    
    return answer


# ==========================================
# Other's Solution
# parent, child의 방문여부 확인

from collections import defaultdict

def solution(info, edges):
    answer = []
    visited = [0] * len(info)
    visited[0] = 1
    graph = defaultdict(list)
    
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    def dfs(sheep, wolf):
        # print(sheep, wolf, visited)
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep+(info[child]^1), wolf+info[child])
                visited[child] = 0

        # 아래와 같이 수정해봤지만 위에가 더 빠른듯
        # for parent in range(len(visited)):
        #     if visited[parent]:
        #         for child in graph[parent]:
        #             if not visited[child]:
        #                 visited[child] = 1
        #                 dfs(sheep+(info[child]^1), wolf+info[child])
        #                 visited[child] = 0
        
    
    dfs(1, 0)
    return max(answer)


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))