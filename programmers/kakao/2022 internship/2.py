# from collections import deque

# def solution(queue1, queue2):
#     answer = -1
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#     sum_q1 = sum(queue1)
#     sum_q2 = sum(queue2)
#     if (sum_q1 + sum_q2) % 2 != 0:
#         return -1
#     target = (sum_q1 + sum_q2) // 2
    
#     results = []

#     def func(i, q1, q2, sum_q1, sum_q2):
#         if sum_q1 == target:
#             results.append(i)
#             return i

#         if q1:
#             val = q1.popleft()
#             q2.append(val)
#             sum_q1 -= val
#             sum_q2 += val
#             func(i + 1, q1, q2, sum_q1, sum_q2)

#             # 원상태로
#             val = q2.pop()
#             q1.appendleft(val)

#         if q2:
#             val = q2.popleft()
#             q1.appendleft(val)
#             sum_q1 += val
#             sum_q2 -= val
#             func(i + 1, q1, q2, sum_q1, sum_q2)
    

#     func(0, queue1, queue2, sum_q1, sum_q2)
#     return answer

from collections import deque
import sys
sys.setrecursionlimit(10**6)

def solution(queue1, queue2):
    answer = -1

    q_size = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    if (sum_q1 + sum_q2) % 2 != 0:
        return -1
    target = (sum_q1 + sum_q2) // 2

    result = 0
    
    while sum_q1 != sum_q2:
        # print(result)
        if result > q_size * 3:
        # if result > len(queue1) * len(queue2):
            return -1
        if sum_q1 < sum_q2:
            val = queue2.popleft()
            queue1.append(val)
            sum_q1 += val
            sum_q2 -= val
        else:
            val = queue1.popleft()
            queue2.append(val)
            sum_q1 -= val
            sum_q2 += val
        result += 1

    return result

