# Test Passed

t = int(input())
for _ in range(t):
	n = int(input())
	v = list(map(int, input().strip().split(" ")))
	# print(v)
	mean = sum(v) / n
	passed = 0
	
	for score in v:
		if score >= mean:
			passed += 1
	
	print(f"{str(passed)}/{str(n)}")
	