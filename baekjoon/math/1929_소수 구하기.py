M, N = map(int, input().split())
num = [0] * (N + 1)

for i in range(2, N):
    if num[i] == 0:
        j = 2
        while j * i < N + 1:
            num[j * i] = 1
            j += 1

for i in range(M, N + 1):
    if num[i] == 0:
        print(i)