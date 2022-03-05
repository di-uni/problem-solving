# First Trial
# Solved (메모리 32360 KB, 시간 100 ms)

from collections import deque

queue = deque()
ans = []

N, K = map(int, input().split())

for i in range(1, N + 1):
    queue.append(i)

while len(queue) > 1:
    queue.rotate(-(K - 1))
    ans.append(queue.popleft())

print("<", end="")
for a in ans:
    print(a, end=", ")
print(f"{queue[0]}>")


# ====================================
# Other's solution
# k만큼 popleft 후 다시 queue에 append
# rotate 쓰는게 나은듯..
# Solved (메모리 32352 KB, 시간 144 ms)

from collections import deque

queue = deque()
ans = []

N, K = map(int, input().split())

for i in range(1, N + 1):
    queue.append(i)

while queue:
    for i in range(K - 1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())

print("<", end="")
for i in range(len(ans) - 1):
    print(ans[i], end=", ")
print(f"{ans[-1]}>")