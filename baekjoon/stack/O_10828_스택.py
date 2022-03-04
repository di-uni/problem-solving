# First Trial
# Solved (메모리 30864 KB, 시간 76 ms)

import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        stack.append(command[1])

    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]

    elif command[0] == "size":
        print(len(stack))

    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
