# 2022.10.06
# First Trial
# Test Passed
# Runtime: faster than 53.30%, Memory Usage: less than 16.08%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return ''.join(reversed(str(x))) == str(x)


# Second Trial
# Test Passed
# Runtime: faster than 73.57%, Memory Usage: less than 59.11%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strx = str(x)
        
        for i in range(len(strx)//2):
            if strx[i] != strx[len(strx)-1-i]:
                return False
        return True


# =================================================================
# Solution by LeetCode
# Space Optimized
# Runtime: faster than 47.30%, Memory Usage: less than 96.33%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        revertedX = 0
        while x > revertedX:
            revertedX = revertedX * 10 + x % 10
            x //= 10
            
        return x == revertedX or x == revertedX // 10