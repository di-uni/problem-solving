# First Trial
# Test Passed

import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    remains = deque([])

    for p, s in zip(progresses, speeds):
        remains.append(math.ceil((100 - p) / s))

    cnt = 1
    temp = temp_max = remains.popleft()

    while len(remains) != 0:
        temp = remains.popleft()
        if temp > temp_max:
            answer.append(cnt)
            cnt = 0
        cnt += 1
        temp_max = max(temp_max, temp)
    answer.append(cnt)


    return answer


# ==============================
# Other's Solution (1)

def solution(progresses, speeds):
    Q = []
    
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1

    return [q[1] for q in Q]