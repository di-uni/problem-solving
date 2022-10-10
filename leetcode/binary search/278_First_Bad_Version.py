# 2022-10-10

# First Trial 

# Time Complexity: O(log n) /   Runtime: faster than 68.62%
# Space Complexity: O(n) /   Memory Usage: less than 62.31% 

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        firstBad = n
        
        while left <= right:
            print(left, right)
            mid = (left + right) // 2
            if isBadVersion(mid):
                firstBad = min(firstBad, mid)
                right = mid - 1
            else:
                left = mid + 1
                
        return firstBad



# =================================================================
# Other's Solution
# Clean code
# Runtime: faster than 12.74%, Memory Usage: less than 62.31%

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        return left