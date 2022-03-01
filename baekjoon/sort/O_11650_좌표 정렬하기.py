N = int(input())
pts = []

for _ in range(N):
    pts.append(list(map(int, input().split())))

# # First Trial
# Solved (메모리 51636 KB, 시간 4556 ms)
pts.sort(key=lambda x: x[1])
pts.sort(key=lambda x: x[0])

# Other's solution #1
# Solved (메모리 51248 KB, 시간 4392 ms)
pts = sorted(pts)

# Other's solution #2
# Solved (메모리 57780 KB, 시간 4468 ms)
pts.sort(key=lambda x: (x[0], x[1]))



for p in pts:
    print(p[0], p[1])