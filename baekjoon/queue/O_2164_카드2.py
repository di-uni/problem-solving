# First Trial
# Solved (메모리 49240 KB, 시간 372 ms)

from collections import deque

N = int(input())
queue = deque()

for i in range(1, N + 1):
    queue.append(i)

while len(queue) > 1:
    # print(queue)
    queue.popleft()
    if len(queue) == 1:
        break
    queue.append(queue.popleft())

print(queue[0])


# ====================================
# Other's solution (1)
# 위 코드를 좀 더 간결하게
# Solved (메모리 53324 KB, 시간 248 ms)

from collections import deque

N = int(input())
queue = deque([i for i in range(1, N + 1)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])


# Other's solution (1)
# 일정한 규칙을 찾아서: https://tooo1.tistory.com/88 
# [input - (input보다 작지만 가장 큰 2의 제곱)] * 2
# Solved (메모리 30864 KB, 시간 68 ms)

N = int(input())
square = 2

while True:
    if (N == 1) or (N == 2):
        print(N)
        break
    square *= 2
    if square >= N:
        print((N - (square // 2)) * 2)
        break