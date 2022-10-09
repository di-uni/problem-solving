# First Trial
# 시간 초과

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    if n == 0:
        if "D" in p:
            input()
            print("error")
        else:
            print(input())
        continue
    array = deque(map(int, input().rstrip().strip('[]').split(',')))
    
    # remove RR
    p = p.replace("RR", "")
    print(p)
    for command in p:
        if command == "R":
            array.reverse()
        if command == "D":
            if len(array) == 0:
                print("error")
                break
            array.popleft()
    else:
        print(list(array))


# Second Trial
# 시간 초과

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
isReversed = False

for _ in range(T):
    p = input()
    n = int(input())
    if n == 0:
        if "D" in p:
            input()
            print("error")
        else:
            print(input().rstrip())
        continue
    array = deque(map(int, input().rstrip().strip('[]').split(',')))
    
    
    for command in p:
        if command == "R":
            isReversed = ~isReversed
        if command == "D":
            if len(array) == 0:
                print("error")
                break
            if isReversed:
                array.pop()
            else:
                array.popleft()
    else:
        if isReversed:
            array.reverse()
        print(list(array))



# 2022.10.09
# Third Trial
# Solved (메모리 32412 KB, 시간 92 ms)
# Referred to other's solution: 출력할 때 join 사용

import sys
from collections import deque, Counter
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    func = input().rstrip()
    func = func.replace("RR", "")
    n = int(input())
    arr = input().rstrip()
    if arr == "[]":
        arr = []
    else:
        arr = deque(arr.strip("[]").split(","))
    toDelete = Counter(list(func))['D']
    if toDelete > n:
        print('error')
        continue
    elif toDelete == n:
        print([])
        continue
    
    isReversed = False
    for p in func:
        if p == 'R':
            isReversed = not isReversed
        elif p == 'D':
            if isReversed:
                arr.pop()
            else:
                arr.popleft()
    if isReversed:
        # print(list(reversed(list(arr))))
        arr.reverse()
    # else:
        # print(arr)
        # print(list(arr))
    print("[" + ",".join(arr) + "]")