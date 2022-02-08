class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # First trial
        # Top-down (Memoization)

        # Time Complexity: O(n) /   Runtime: faster than 35.24%
        # Space Complexity: O(n) /   Memory Usage: less than 16.34%

        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
            
        memo_first = {}
        memo_last = {}
        nums_first = nums[:n-1]
        nums_last = nums[1:]
        
        # print(nums_first, nums_last)
        
        def dp(i, memo, nums_list):
            if i == 0:
                return nums_list[0]
            if i == 1:
                return max(nums_list[0], nums_list[1])
            if i not in memo:
                memo[i] = max(dp(i-1, memo, nums_list), dp(i-2, memo, nums_list) + nums_list[i])
            return memo[i]
        
        # print(dp(n - 2, memo_last, nums_last), dp(n - 2, memo_first, nums_first))
        return max(dp(n - 2, memo_last, nums_last), dp(n - 2, memo_first, nums_first))

    # -----------------------------------------------------------------
        # Second trial refer to DP lecture
        # Bottom-up (Tabulation)

        # Time Complexity: O(n) /   Runtime: faster than 50.89%
        # Space Complexity: O(n) /   Memory Usage: less than 43.69%

        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        # print(nums_first, nums_last)
        
        def simple_rob(nums_list):
            temp = [0] * len(nums_list)
            temp[0] = nums_list[0]
            temp[1] = max(nums_list[0], nums_list[1])
            for i in range(2, len(nums_list)):
                temp[i] = max(temp[i-1], temp[i-2] + nums_list[i])
            return temp[len(nums_list)-1]
        
        return max(simple_rob(nums[:n-1]), simple_rob(nums[1:]))