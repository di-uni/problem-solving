class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        
        # First trial (get some hints from lesson)
        # Time Limit Exceeded Error

        n = len(nums)
        m = len(multipliers)
        
        def score(i, left):
            # print(i, left)
            right = left + (n - 1) - i
            mult = multipliers[i]
            
            if i == m - 1:
                return max(nums[right]*mult, nums[left]*mult)
            return max(score(i+1, left) + nums[right]*mult, score(i+1, left+1) + nums[left]*mult)
        
        return score(0, 0)

    # -----------------------------------------------------------------
        # Second trial (get some hints from lesson)
        # Top-down (Memoization)
        # Time Limit Exceeded Error

        # Time Complexity: O(n) /   Runtime: faster than 57.61%
        # Space Complexity: O(n) /   Memory Usage: less than 22.90%

        n = len(nums)
        m = len(multipliers)
        dp = [[None for x in range(m)] for y in range(n)]
        # print(dp)
        
        def score(i, left):
            # print(i, left)
            if dp[i][left] == None:
                right = left + (n - 1) - i
                mult = multipliers[i]
                if i == m - 1:
                    dp[i][left] = max(nums[right]*mult, nums[left]*mult)
                else:
                    dp[i][left] = max(score(i+1, left) + nums[right]*mult, score(i+1, left+1) + nums[left]*mult)
            return dp[i][left]
        
        return score(0, 0)

     # -----------------------------------------------------------------
        # Third trial (get some hints from lesson)
        # Bottom-up (Tabulation)

        # Time Complexity: O(n^2) /   Runtime: faster than 68.07%
        # Space Complexity: O(n^2) /   Memory Usage: less than 68.07%

        n = len(nums)
        m = len(multipliers)
        dp = [[0] * m for x in range(m)]
        
        for i in range(m - 1, -1, -1): 
            for left in range(i, -1, -1):
                right = left + (n - 1) - i
                mult = multipliers[i]
                if i == m - 1:
                    dp[i][left] = max(nums[right]*mult, nums[left]*mult)
                else:
                    dp[i][left] = max(dp[i+1][left] + nums[right]*mult, dp[i+1][left+1] + nums[left]*mult)
        
        return dp[0][0]