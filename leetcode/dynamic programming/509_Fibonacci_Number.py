# 2022.10.13
# First Trial
# Test Passed
# Runtime: faster than 61.14%, Memory Usage: less than 55.10%

class Solution:
    def fib(self, n: int) -> int:
        # if n == 0 or n == 1:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)
        
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        
        return dp[n]


# =================================================================
# Other's Solution
# Space Optimized
# Runtime: faster than 35.24%, Memory Usage: less than 55.00%

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        
        dp = (0, 1)
        for i in range(2, n + 1):
            dp = (dp[1], dp[0] + dp[1])
        
        return dp[1]

        