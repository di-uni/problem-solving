class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        # First trial (get some hints from discussion)
        # Top-down (Memoization)

        # Time Complexity: O(n) /   Runtime: faster than 28.32%
        # Space Complexity: O(n) /   Memory Usage: less than 8.23%

        memo = {}
        
        def dp(i):
            if i <= 1:
                return cost[i]
            if i == len(cost):
                memo[i] = min(dp(i-1), dp(i-2))
            if i not in memo:
                memo[i] = cost[i] + min(dp(i-1), dp(i-2)) 
                # Previously I wrote here: "min(dp(i-1), dp(i-2) + cost[i])"
            return memo[i]
        
        dp(len(cost))
        return memo

    # -----------------------------------------------------------------
        # Second trial refer to other's solution
        # Bottom-up (Tabulation)

        # Time Complexity: O(n) /   Runtime: faster than 57.61%
        # Space Complexity: O(n) /   Memory Usage: less than 22.90%

        dp = []
        cost.append(0)
        dp.append(cost[0])
        dp.append(cost[1])
        for i in range(2, len(cost)):
            dp.append(cost[i] + min(dp[i-1], dp[i-2]))
        return dp[len(cost)-1]

    # -----------------------------------------------------------------
        # Third trial refer to other's solution
        # Bottom-up (Tabulation)

        # Time Complexity: O(n) /   Runtime: faster than 26.85%
        # Space Complexity: O(1) /   Memory Usage: less than 81.48%

        first = cost[0]
        second = cost[1]
        if len(cost) <= 2:
            return min(first, second)
        
        for i in range(2, len(cost)):
            curr = cost[i] + min(first, second)
            first = second
            second = curr
        return min(first, second)