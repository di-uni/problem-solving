# First Trial
# 87% (didn't consider empty input: ([], 0))

from collections import deque

def solution(A, K):
    if K % len(A) == 0:
        return A
    
    K = K % len(A)
    queue = deque(A)
    
    if K < (len(A) // 2):
        for _ in range(K):
            queue.appendleft(queue.pop())    
            # print(queue)    
    else:
        for _ in range(len(A) - K):
            queue.append(queue.popleft()) 

    return list(queue)


# Second Trial
# 100%

from collections import deque

def solution(A, K):
    if K == [] or A == 0:
        return A
        
    if K % len(A) == 0:
        return A
    
    K = K % len(A)
    queue = deque(A)
    
    if K < (len(A) // 2):
        for _ in range(K):
            queue.appendleft(queue.pop())    
            # print(queue)    
    else:
        for _ in range(len(A) - K):
            queue.append(queue.popleft()) 

    return list(queue)