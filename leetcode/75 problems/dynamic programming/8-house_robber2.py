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
    
    # -----------------------------------------------------------------
    # 2022-03-02

    # Top-down

        # Time Complexity: O(n) /   Runtime: faster than 84.15%
        # Space Complexity: O(n) /   Memory Usage: less than 5.6% 
        
        def robORnot(i, _nums, memo):
            if i == 0:
                return _nums[0]
            elif i == 1:
                return max(_nums[0:2])
            else:            
                if i not in memo:
                    memo[i] = max(robORnot(i - 1, _nums, memo), robORnot(i - 2, _nums, memo) + _nums[i])
                return memo[i]
        
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0:2])
        else:
            memo1 = {}
            memo2 = {}
            return max(robORnot(n - 2, nums[:n-1], memo1), robORnot(n - 2, nums[1:], memo2))


        # Bottom-up

        # Time Complexity: O(n) /   Runtime: faster than 56.45%
        # Space Complexity: O(n) /   Memory Usage: less than 69.74% 

        def tab(_nums):
            n = len(_nums)
            money = [0] * n
            money[0] = _nums[0]
            money[1] = max(_nums[:2])

            for i in range(2, n):
                money[i] = max(money[i - 2] + _nums[i], money[i - 1])
            return money[n - 1]
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[:2])
        
        return max(tab(nums[:n-1]), tab(nums[1:]))