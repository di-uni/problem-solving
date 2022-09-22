# ==========================================
# Other's Solution
# Test Passed

import heapq as hq

def solution(jobs):
    answer = 0
    start, now = -1, 0
    heap = []
    
    i = 0
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                hq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            target = hq.heappop(heap)
            i += 1
            start = now
            now += target[0]
            answer += now - target[1]
        else:
            now += 1
    
    return answer // len(jobs)