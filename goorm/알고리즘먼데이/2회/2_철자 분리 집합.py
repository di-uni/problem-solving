# Test Passed

n = int(input())
s = input()

prev = ""
ans = 0
for char in s:
	if char != prev:
		ans += 1
		prev = char
	
print(ans)