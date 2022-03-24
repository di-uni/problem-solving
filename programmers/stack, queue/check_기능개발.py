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