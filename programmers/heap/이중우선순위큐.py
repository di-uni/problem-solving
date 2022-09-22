# First Trial
# Test Passed

import heapq as hq

def solution(operations):
    answer = [0, 0]
    heap = []
    
    for op in operations:
        if op[0] == "I":
            op, num = op.split(" ")
            hq.heappush(heap, int(num))
        elif len(heap) > 0:
            if op == "D 1":
                heap = hq.nlargest(len(heap), heap)[1:]
                hq.heapify(heap)
                # heap.remove(max(heap))
            elif op == "D -1":
                hq.heappop(heap)
    
    if heap:
        answer[0] = hq.nlargest(1, heap)[0]
        # answer[0] = max(heap)
        answer[1] = heap[0]
        
                
    return answer


# ======================================
# Other's solution 
# 두 개의 queue 사용

import heapq as hq

def solution(operations):
    heap = []
    max_heap = []
    
    for op in operations:
        if op[0] == "I":
            operand = int(op.split(" ")[1])
            hq.heappush(heap, operand)
            hq.heappush(max_heap, (operand *(-1), operand))
        elif len(heap) > 0:
            if op == "D 1":
                max_val = hq.heappop(max_heap)[1]
                heap.remove(max_val)
            elif op == "D -1":
                min_val = hq.heappop(heap)
                max_heap.remove((min_val*(-1), min_val))
    
        
    if heap:            
        return [max_heap[0][1], heap[0]]
    else:
        return [0, 0]