import sys

N = int(sys.stdin.readline().rstrip())
num = [0] * 10001

for i in range(N):
    num[int(sys.stdin.readline().rstrip())] += 1

for i, cnt in enumerate(num):
    for c in range(cnt):
        print(i)