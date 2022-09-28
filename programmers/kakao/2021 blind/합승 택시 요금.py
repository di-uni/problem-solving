# ==========================================
# Other's Solution
# using dijkstra

from heapq import heappop, heappush
from collections import defaultdict

def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = defaultdict(list)
    
    for src, dst, cost in fares:
        graph[src].append([dst, cost])
        graph[dst].append([src, cost])
        
    def dijkstra(src, dst):
        table = [INF for i in range(n+1)]
        table[src] = 0
        queue = [[0, src]]
        
        while queue:
            w, x = heappop(queue)
            
            if table[x] < w: continue
            
            for nx, ncost in graph[x]:
                ncost += w
                if ncost < table[nx]:
                    table[nx] = ncost
                    heappush(queue, [ncost, nx])
        
        # print(table, table[dst])
        return table[dst]
    
    min_cost = INF
    for i in range(1, n+1):
        # print(i)
        min_cost = min(min_cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    
    return min_cost

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))