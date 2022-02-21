T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    Y = N % H          # floor
    X = N // H + 1     # number
    if Y == 0:
        # Y = int(N / H)
        # Y = N
        X -= 1
    if X < 10:
        X = "0" + str(X)
    print(str(Y) + str(X))