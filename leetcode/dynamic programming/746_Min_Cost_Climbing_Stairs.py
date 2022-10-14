# First trial (get some hints from discussion)
# Top-down (Memoization)

# Time Complexity: O(n) /   Runtime: faster than 28.32%
# Space Complexity: O(n) /   Memory Usage: less than 8.23%

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
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



# 2022.10.14
# First trial 
# Top-down (Memoization)

# Time Complexity: O(n) /   Runtime: faster than 28.32%
# Space Complexity: O(n) /   Memory Usage: less than 8.23%

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        return min(dp[n - 1], dp[n - 2])


# -----------------------------------------------------------------
# Other's Solution (1)
# Bottom-up (Tabulation)

# Time Complexity: O(n) /   Runtime: faster than 57.61%
# Space Complexity: O(n) /   Memory Usage: less than 22.90%

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []
        cost.append(0)
        dp.append(cost[0])
        dp.append(cost[1])
        for i in range(2, len(cost)):
            dp.append(cost[i] + min(dp[i-1], dp[i-2]))
        return dp[len(cost)-1]


# -----------------------------------------------------------------
# Other's Solution (2)
# Bottom-up (Tabulation)

# Time Complexity: O(n) /   Runtime: faster than 26.85%
# Space Complexity: O(1) /   Memory Usage: less than 81.48%

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        if len(cost) <= 2:
            return min(first, second)
        
        for i in range(2, len(cost)):
            curr = cost[i] + min(first, second)
            first = second
            second = curr
        return min(first, second)

