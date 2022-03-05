# First Trial
# 모든 연산이 O(1)이어야 함. pop(0)은 O(1)이 아님
# 시간 초과

import sys
queue = []

for _ in range(int(input())):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        queue.append(command[1])
        continue
    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))     # 0th element pop
        continue
    elif command[0] == "size":
        print(len(queue))
        continue
    elif command[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
        continue
    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
        continue
    elif command[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
        continue


# Second Trial (Hint: Using deque library or linked list)
# with deque
# Solved (메모리 141632 KB, 시간 1944 ms)

import sys
from collections import deque
queue = deque()

for _ in range(int(input())):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        queue.append(command[1])
        continue
    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft()) 
        continue
    elif command[0] == "size":
        print(len(queue))
        continue
    elif command[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
        continue
    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
        continue
    elif command[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
        continue


# Third Trial (Hint: Using deque library or linked list)
# with linked list