# First Trial
# Solved (메모리 32396 KB, 시간 96 ms)

from collections import deque

N, M = map(int, input().split())
queue = deque([i for i in range(1, N + 1)])
target = list(map(int, input().split()))
ans = 0

for t in target:
    if t == queue[0]:
        queue.popleft()
    else:
        right = 0
        for i in range(len(queue)):
            if t == queue[0]:
                break
            queue.rotate(1)
            right += 1
        ans += min(len(queue) - right, right)
        queue.popleft()


print(ans)
            

# =============================================
# Other's Solution
# 1 ~ N deque 간략히, index 이용
# Solved (메모리 32368 KB, 시간 84 ms)

from collections import deque

N, M = map(int, input().split())
queue = deque(range(1, N + 1))
target = list(map(int, input().split()))
ans = 0

for t in target:
    mid = len(queue) // 2
    if queue.index(t) > mid:
        while t != queue[0]:
            queue.appendleft(queue.pop())
            ans += 1
        queue.popleft()
    else:
        while t != queue[0]:
            queue.append(queue.popleft())
            ans += 1
        queue.popleft()
print(ans)