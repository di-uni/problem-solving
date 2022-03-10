# First Solution
# Bottom-up
# Solved (메모리 30860 KB, 시간 76 ms)

T = int(input())
pado = [1,1,1,2,2]

for _ in range(T):
    N = int(input())
    for i in range(len(pado), N):
        pado.append(pado[i - 1] + pado[i - 5])
    # print(pado)
    print(pado[N - 1])