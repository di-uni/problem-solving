class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # First trial refer to DP lecture
        # Top-down (Memoization)

        # Time Complexity: O(n) /   Runtime: faster than 15.43%
        # Space Complexity: O(n) /   Memory Usage: less than 6.41%

        memo = {}
        
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]
            
        return dp(len(nums) - 1)

    # -----------------------------------------------------------------
        # Second trial refer to DP lecture
        # Bottom-up (Tabulation)

        # Time Complexity: O(n) /   Runtime: faster than 32.98%
        # Space Complexity: O(n) /   Memory Usage: less than 91.44%

        n = len(nums)
        if n == 1:
            return nums[0]
        # unneccessary
        # if n == 2:
        #     return max(nums[0], nums[1])
        
        ans = [0] * n
        ans[0] = nums[0]
        ans[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            ans[i] = max(ans[i-1], ans[i-2] + nums[i])
            
        return ans[n - 1]


    # -----------------------------------------------------------------
    # 2022-03-02
        # Top-down

        # Time Complexity: O(n) /   Runtime: faster than 26.61%
        # Space Complexity: O(n) /   Memory Usage: less than 19.09% 

        memo = {}
        
        def robORnot(n):
            if n == 0:
                return nums[0]
            elif n == 1:
                return max(nums[:2])
            if n not in memo:
                memo[n] = max(robORnot(n - 2) + nums[n], robORnot(n - 1))
            return memo[n]
        
        return robORnot(len(nums) - 1)



        # Bottom-up

        # Time Complexity: O(n) /   Runtime: faster than 33.30%
        # Space Complexity: O(n) /   Memory Usage: less than 19.09% 

        n = len(nums)
    
        if n == 1:
            return nums[0]
        
        money = [0] * n
        money[0] = nums[0]
        money[1] = max(nums[:2])


        for i in range(2, n):
            money[i] = max(money[i - 2] + nums[i], money[i - 1])
        # print(money)
        return money[n - 1]
            


    