class Solution(object):

    # First trial (similar to fibonacci problem - climbing stairs)
    # Dictionary memoization
    
    # Time Complexity: O(n) /   Runtime: faster than 59.94%
    # Space Complexity: O(n) /   Memory Usage: less than 65.33%

    def __init__(self):
        self.memo = {0:0, 1:1, 2:1}
    
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.memo:
            self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.memo[n]
        