# Test Passed

def getRoutes(n, edges):
	cnt = 1
	edges = list(map(int, edges.split(" ")))
	for edge in edges:
		cnt *= edge
	
	return cnt

def main():
	n = input()
	edges = input()
	print(getRoutes(n, edges))

if __name__ == "__main__":
	main()

