# First Trial
# Test Failed (RecursionError: maximum recursion depth exceeded in comparison)

from collections import deque
def solution(n, start, end, roads, traps):
    answer = []
    
    def bfs(i, time, roads):
        queue = deque([])
        
        if i == end:
            print(time)
            answer.append(time)
            return time
        
        for r in roads:
            if r[0] == i:
                queue.append(r)
        
        while queue:
            road = queue.popleft()
            next_node = road[1]
            if next_node in traps:
                for idx in range(len(roads)):
                    if roads[idx][0] == next_node or roads[idx][1] == next_node:
                        temp = roads[idx][0]
                        roads[idx][0] = roads[idx][1]
                        roads[idx][1] = temp
            bfs(next_node, time + road[2], roads)
            
    print(bfs(start, 0, roads))
    return answer