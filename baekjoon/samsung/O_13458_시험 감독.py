# First Trial
# Solved (메모리 149432 KB, 시간 888 ms)

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0

for i in range(N):
    A[i] -= B
    cnt += 1
    if A[i] < 0:
        continue
    cnt += A[i] // C
    if A[i] % C != 0:
        cnt += 1

print(cnt)