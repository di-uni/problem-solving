def solution(numbers):
    answer = ''
    nums = [str(n) for n in numbers]
    nums.sort()
    # nums.sort(reverse="True")
    
    # print(nums)
    
    for i in range(1, len(numbers)):
        # print(nums, nums[i - 1], nums[i])
        if nums[i - 1][0] == nums[i][0]:
            if len(nums[i-1]) == len(nums[i]):
                a = nums[i-1][-1]
                b = nums[i][-1]
            else:
                l = min(len(nums[i-1]), len(nums[i]))
                if len(nums[i-1]) == l:
                    a = nums[i-1][0]
                    b = nums[i][l]
                else:
                    a = nums[i-1][l]
                    b = nums[i][0]
                if a > b:   # swiping
                    temp = nums[i - 1]
                    nums[i - 1] = nums[i]
                    nums[i] = temp
            
    # print(nums)
    for i in range(len(numbers) - 1, -1, -1):
        if answer == "0" and nums[i] == "0":
            return "0"
        answer += nums[i]
        
    return answer