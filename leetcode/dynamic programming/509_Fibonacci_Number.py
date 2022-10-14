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