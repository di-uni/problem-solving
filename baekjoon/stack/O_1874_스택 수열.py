# First Trial
# Solved (메모리 35516 KB, 시간 4076 ms)

from collections import deque

n = int(input())
elems = deque()
stack = []
ans = []

for _ in range(n):
    elems.append(int(input()))

for i in range(1, n + 1):
    stack.append(i)
    ans.append("+")
    while stack and (elems[0] == stack[-1]):
        elems.popleft()
        stack.pop()
        ans.append("-")

if stack:
    print("NO")
else:
    for a in ans:
        print(a)


# =====================================
# Other's Solution
# Solved (메모리 35516 KB, 시간 4364 ms)

n = int(input())
stack = []
ans = []
flag = 0
cur = 1

for i in range(n):
    num = int(input())

    while cur <= num:
        stack.append(cur)
        ans.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    print("\n".join(ans))