# ==========================================
# Other's Solution
# using dijkstra only once

from collections import defaultdict
from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    INF = int(1e9)
    graph = defaultdict(list)
    
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    def get_min_intensity():
        table = [INF] * (n + 1)
        queue = []
        
        for gate in gates:
            heappush(queue, (0, gate))
            table[gate] = 0
        
        while queue:
            intensity, x = heappop(queue)
            
            # set(summits)은 hash 함수 이용해서 저장하기 때문에 원소 검색이 O(1)
            if x in set_summits or table[x] < intensity: 
                continue
            
            for nx, weight in graph[x]:
                new_intensity = max(weight, intensity)
                if new_intensity < table[nx]:
                    table[nx] = new_intensity
                    heappush(queue, (new_intensity, nx))
        
        res_summit = 0
        min_intensity = INF
        for summit in summits:
            if table[summit] < min_intensity:
                res_summit = summit
                min_intensity = table[summit]
                
        return [res_summit, min_intensity]
    
    summits.sort()
    set_summits = set(summits)
    return get_min_intensity()