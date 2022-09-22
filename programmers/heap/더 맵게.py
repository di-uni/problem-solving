# Second Trial
# Test Passed

from heapq import heappush, heappop

def solution(scoville, K):
    cnt = 0
    heap = []
    
    for sc in scoville:
        heappush(heap, sc)
    
    # print(heap)
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        heappush(heap, heappop(heap) + heappop(heap) * 2)
        cnt += 1
        
    return cnt


# Second Trial
# Test Passed
# heapify 사용

from heapq import heapify, heappush, heappop

def solution(scoville, K):
    cnt = 0
    heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        cnt += 1
        
    return cnt