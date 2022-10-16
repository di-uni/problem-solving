# Test Failed

from collections import defaultdict

N, k = map(int, input().strip().split(" "))
attendance = defaultdict(list)
order = {}

for i in range(N):
	info = input().strip().split(" ")
	name, height = info[0], float(info[1])
	if name not in attendance:
		order[i + 1] = name
	attendance[name].append(height)

for i in range(k, -1, -1):
	if i in order:
		name = order[i]
		heights = sorted(attendance[name])
		# heights[k - i]
		print(f"{name} {heights[k - i]:.2f}")
		break

