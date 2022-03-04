import sys
K = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(K):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))

