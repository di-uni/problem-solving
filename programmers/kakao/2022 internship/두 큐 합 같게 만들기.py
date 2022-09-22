# deque를 이용하는 방법

from collections import deque

def solution(queue1, queue2):
    count = 0
    que1 = deque(queue1)
    que2 = deque(queue2)
    limit = 4 * len(queue1)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    
    if (tot1 + tot2) % 2 != 0:
        return -1
    
    while True:
        if count > limit:
            return -1
        if tot1 > tot2:
            target = que1.popleft()
            que2.append(target)
            tot1 -= target
            tot2 += target
            count += 1
        elif tot1 < tot2:
            target = que2.popleft()
            que1.append(target)
            tot2 -= target
            tot1 += target
            count += 1
        else:
            break
    return count


# 투 포인터를 이용하는 방법

def solution(queue1, queue2):
    count = 0
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    tot_queue = queue1 + queue2
    start1, start2 = 0, len(queue1)
    limit = 4 * len(queue1)
    
    if (tot1 + tot2) % 2 != 0:
        return -1
    
    while True:
        if count > limit:
            return -1
        if tot1 > tot2:
            target = tot_queue[start1]
            start1 += 1
            if (start1 >= 2 * len(queue1)):
                start1 = 0
            tot1 -= target
            tot2 += target
            count += 1
        elif tot1 < tot2:
            target = tot_queue[start2]
            start2 += 1
            if (start2 >= 2 * len(queue1)):
                start2 = 0
            tot2 -= target
            tot1 += target
            count += 1
        else:
            break
    return count