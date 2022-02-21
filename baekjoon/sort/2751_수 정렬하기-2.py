import sys

N = int(sys.stdin.readline().rstrip())
num = []

for i in range(N):
    num.append(int(sys.stdin.readline().rstrip()))
num.sort()
for n in num:
    print(n)