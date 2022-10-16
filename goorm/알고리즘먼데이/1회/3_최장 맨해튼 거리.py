# Test Passed

def getLongestManhattan(nums):
	nums.sort()
	return -nums[0]-nums[1]+nums[2]+nums[3]

def main():
	nums = list(map(int, input().split(" ")))
	print(getLongestManhattan(nums))

if __name__ == "__main__":
	main()


# Answer
import sys
input = sys.stdin.readline
arr = list(map(int, input().split()))
arr.sort()
print(arr[3] + arr[2] - arr[1] - arr[0])