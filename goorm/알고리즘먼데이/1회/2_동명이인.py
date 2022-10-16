# Test Passed

def countSimilarNames(name, names):
	cnt = 0
	for n in names:
		if name in n:
			cnt += 1
	
	return cnt

def main():
	n, name = input().split(" ")
	names = []
	for i in range(int(n)):
		names.append(input())
	# print(names)
	print(countSimilarNames(name, names))

if __name__ == "__main__":
	main()