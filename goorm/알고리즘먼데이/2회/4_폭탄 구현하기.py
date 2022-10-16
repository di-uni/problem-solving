# Test Passed

n, k = map(int, input().strip().split(" "))
grid = [[0] * n for _ in range(n)]
ans = 0

for _ in range(k):
	a, b = map(int, input().strip().split(" "))
	grid[a-1][b-1] += 1

for x in range(n):
	for y in range(n):
		cnt = grid[x][y]
		ans += cnt
		for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
			if 0 <= x + dx < n and 0 <= y + dy < n:
				ans += cnt

print(ans)