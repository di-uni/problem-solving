# First Trial
# Wrong Answer

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

# Second Trial
# Solved (메모리 30864 KB, 시간 92 ms)

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    if floor == 0:
        floor = H
    ans = str(floor)   # floor
    num = (N - 1) // H + 1  # room number
    if num < 10:
        ans += "0" + str(num)
    else:
        ans += str(num)
    print(ans)

# =========================
# Other's solution
# floor에 100을 곱한 후 num을 더하면 더 간단히 구할 수 있다.
# Solved (메모리 30864 KB, 시간 80 ms)

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    if floor == 0:
        floor = H
    num = (N - 1) // H + 1 
    print(f'{floor*100+num}')