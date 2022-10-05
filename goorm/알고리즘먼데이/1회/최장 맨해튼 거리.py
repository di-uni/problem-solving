# Test Failed

def getLongestManhattan(nums):
# 	idx = [1, 2, 3]
# 	longest = 0
	
# 	for j in range(1, 4):
# 		abs_y = []
# 		# print("j:", j)
# 		for k in idx:
# 			if k != j:
# 				abs_y.append(nums[k])
# 				print("k:", k)
# 		y1, y2 = abs_y
# 		longest = max(longest, abs(nums[0]-nums[j]) + abs(y1-y2))
# 		print(longest)
	
# 	return longest
	nums.sort()
	return -nums[0]-nums[1]+nums[2]+nums[3]

def main():
	nums = list(map(int, input().split(" ")))
	print(getLongestManhattan(nums))

if __name__ == "__main__":
	main()