# First Trial
# 시간 초과

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

for i in range(2, int(max(nums) ** 0.5) + 1):
# for i in range(2, int(min(nums) ** 0.5) + 1):
    temp = nums[0] % i
    for n in range(2, len(nums)):
        if temp != nums[n] % i:
            break
    else:
        print(i, end=" ")