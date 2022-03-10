# First Trial
# Solved (메모리 30864 KB, 시간 84 ms)

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
            print(queue[0])
            del queue[0]
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


# ================================================
# Other's Solution
# push 시 리스트 맨 앞에 insert해서 python 내장 pop 사용
# Solved (메모리 30864 KB, 시간 84 ms)

import sys
queue = []

for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == "push":
        queue.insert(0, cmd[1])
        continue
    elif cmd[0] == "pop":
        if len(queue) == 0: print(-1)
        else: print(queue.pop())
        continue
    elif cmd[0] == "size":
        print(len(queue))
        continue
    elif cmd[0] == "empty":
        if queue: print(0)
        else: print(1)
        continue
    elif cmd[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[-1])
        continue
    elif cmd[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[0])
        continue
