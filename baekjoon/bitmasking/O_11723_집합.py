# First Trial
# Using set
# 시간 초과

import sys

M = int(sys.stdin.readline().rstrip())
S = set([])

for _ in range(M):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == "add":
        S |= set(cmd[1])
    elif cmd[0] == "remove":
        # if cmd[1] in S:
        #     S.remove(cmd[1])
        S.discard(cmd[1])
    elif cmd[0] == "check":
        # print(cmd[1])
        if cmd[1] in S:
            print(1)
        else: print(0)
    elif cmd[0] == "toggle":
        if cmd[1] in S:
            S.remove(cmd[1])
        else:
            S |= set(cmd[1])
    elif cmd[0] == "all":
        S = set([str(i) for i in range(1, 21)])
        # print(S)
    elif cmd[0] == "empty":
        S = set([])


# Second Trial
# Using bitmasking
# Solved (메모리 30864 KB, 시간 3988 ms)

import sys

M = int(sys.stdin.readline().rstrip())
S = [False] * 21

for _ in range(M):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == "add":
        S[int(cmd[1])] = 1
    elif cmd[0] == "remove":
        S[int(cmd[1])] = 0
    elif cmd[0] == "check":
        if S[int(cmd[1])] == 1:
            print(1)
        else: print(0)
    elif cmd[0] == "toggle":
        if S[int(cmd[1])] == 1:
            S[int(cmd[1])] = 0
        else:
            S[int(cmd[1])] = 1
    elif cmd[0] == "all":
        S = [True] * 21
    elif cmd[0] == "empty":
        S = [False] * 21



# =======================================================
# Other's solution
# cmd 길이에 따라 분기해줌으로써 First Trial을 보완 
# 시간 초과

import sys

M = int(sys.stdin.readline().rstrip())
S = set([])

for _ in range(M):
    cmd = sys.stdin.readline().rstrip().split()
    if len(cmd) == 1:
        if cmd[0] == "all":
            S = set([str(i) for i in range(1, 21)])
        elif cmd[0] == "empty":
            S = set([])
        continue
    else:
        if cmd[0] == "add":
            S.add(cmd[1])
        elif cmd[0] == "remove":
            S.discard(cmd[1])
        elif cmd[0] == "check":
            if cmd[1] in S:
                print(1)
            else: print(0)
        elif cmd[0] == "toggle":
            if cmd[1] in S:
                S.remove(cmd[1])
            else:
                S.add(cmd[1])
