# 2022.10.14
# First trial
# Top-down (Memoization)

# Time Complexity: O(m x n) /   Runtime: faster than 79.45%
# Space Complexity: O(m x n) /   Memory Usage: less than 31.98%

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] + [0] * (n - 1) for _ in range(m)]
        dp[0] = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp[m - 1][n - 1]


# =================================================================
# Other's Solution (1)
# Space Optimized
# Runtime: faster than 40.60%, Memory Usage: less than 74.15%

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp, prevDp = [1] * n, [1] * n
    
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] = dp[i - 1] + prevDp[i]
            prevDp = dp
        
        return dp[n - 1]



# =================================================================
# Other's Solution (2)
# Math (m+n-2)C(n-1): 로봇이 지나가는 발판 수 m+n-2개 중 아래 방향를 선택해야하는 발판의 개수(m-1)
# Runtime: faster than 97.41%, Memory Usage: less than 74.15%

from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))