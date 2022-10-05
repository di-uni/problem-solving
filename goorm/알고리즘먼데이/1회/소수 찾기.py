# Test Passed

def main():
	res = 0
	n = int(input())
	nums = list(map(int, input().split(" ")))
	
	primes = [False if i % 2 == 0 else True for i in range(n + 1)]
	primes[1] = False
	primes[2] = True
	for i in range(3, int((n + 1)**(1/2))+1, 2):
		for j in range(i*2, n+1, i):
			primes[j] = False
	# print(primes)
	
	for idx, num in enumerate(nums):
		if primes[idx+1]:
			# print(num)
			res += num
	
	print(res)

if __name__ == "__main__":
	main()