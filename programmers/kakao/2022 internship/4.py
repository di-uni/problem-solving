import sys
sys.setrecursionlimit(10**6)

def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n + 1)]
    visited = [False] * len(summits)

    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    def dfs(start, i, summit, intensity):
        print(start, i, summit, intensity)
        if summit != None and start == i:
            return [summit, intensity]
        if start != i and i in gates:
            return
        for p, w in graph[i]:
            if p in summits:
                if summit == None:
                    dfs(start, p, p, max(intensity, w))
                else:
                    continue
            else:
                dfs(start, p, summit, max(intensity, w))
        
    for gate in gates:
        print(dfs(gate, gate, None, 0))
    
    return answer


solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])
# solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])