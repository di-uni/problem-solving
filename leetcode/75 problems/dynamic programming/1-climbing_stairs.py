class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # First trial
        # Time Limit Exceeded

        # fibonacci
        
        dp = {}
        def fib(_n):
            if _n in dp:
                return dp[_n]
            if _n == 0 or _n == 1:
                return 1
            return fib(_n-1) + fib(_n-2)
        
        return fib(n)

    # -----------------------------------------------------------------
        # REVISED First trial refer to Third trial
       
        # Time Complexity: O(n) /   Runtime: faster than 58.30%
        # Space Complexity: O(n) /   Memory Usage: less than 66.42%

        dp = {}
        dp[1] = 1
        dp[2] = 2
        def fib(_n):
            if _n not in dp:
                dp[_n] = fib(_n-1) + fib(_n-2)
            return dp[_n]
        
        return fib(n)

    # -----------------------------------------------------------------
        # Second trial refer to other's solution
        # Time Limit Exceeded

        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # -----------------------------------------------------------------
        # Third trial refer to other's solution
        # Dictionary memoization
        
        # Time Complexity: O(n) /   Runtime: faster than 81.62%
        # Space Complexity: O(n) /   Memory Usage: less than 37.82%
    
    def __init__(self):
        self.dic = {}
        self.dic[1] = 1
        self.dic[2] = 2

    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]

    # -----------------------------------------------------------------
        # Forth trial refer to other's solution
        # Tabulation
        
        # Time Complexity: O(n) /   Runtime: faster than 81.62%
        # Space Complexity: O(n) /   Memory Usage: less than 37.82%

        if n <= 2:
            return n
        
        ans = [1] * n
        ans[1] = 2
        
        for i in range(2, n):
            ans[i] = ans[i - 1] + ans[i - 2]
        # print(ans)
        return ans[n - 1]