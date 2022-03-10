import sys
deque = []
# # Other's solution
# from collections import deque
# deque = deque()

for _ in range(int(input())):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push_front":
        deque.insert(0, command[1])
        # # Other's solution
        # deque.appendleft(command[1])
        continue
    elif command[0] == "push_back":
        deque.append(command[1])
        continue
    elif command[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            del deque[0]
            # # Other's solution
            # print(deque.popleft())
        continue
    elif command[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
        continue
    elif command[0] == "size":
        print(len(deque))
        continue
    elif command[0] == "empty":
        if deque:
            print(0)
        else:
            print(1)
        continue
    elif command[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
        continue
    elif command[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
        continue