# First Trial
# Test Passed

from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    max_val = max(queue)
    cnt = 0

    while queue:
        # print(queue, location)
        if max_val > queue[0]:
            queue.rotate(-1)
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1
        if max_val == queue[0]:
            queue.popleft()
            cnt += 1
            if location == 0:
                return cnt
            location -= 1
            if queue:
                max_val = max(queue)


# ==============================
# Other's Solution (1)

def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            # any(): 하나라도 True인게 있으면 True
            # all(): 모두 True여야 True
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


# ==============================
# Other's Solution (2)

def solution(priorities, location):
    answer = 0
    search, c = sorted(priorities, reverse=True), 0

    while True:   
        for i, priority in enumerate(priorities):
            print(i, priority)
            s = search[c]
            if priority == s:
                c += 1
                answer += 1
                if i == location:
                    break   # for문 빠져나오기
        else:   # (for문 내에서) break에 안 걸린 경우
            continue
        break   # for문을 빠져나온 경우 while문도 빠져나오기
    return answer

print(solution([1,1,9,1,1,1], 0))