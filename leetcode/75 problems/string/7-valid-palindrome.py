# 2022.09.29
# First Trial
# Test Passed 
# Runtime: faster than 10.11%, Memory Usage: less than 85.40%

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        
        for elem in s:
            if not elem.isalnum():
                continue
            if elem.isalpha() and elem.isupper():
                newS += elem.lower()
            else:
                newS += elem

        for i in range(int((len(newS)+1)//2)):
            if newS[i] != newS[len(newS)-1 -i]:
                return False
        return True
    


# =================================================================
# Other's Solution
# Using two pointer
# Runtime: faster than 11.60%, Memory Usage: less than 85.40%

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True



# Shortest 
# Runtime: faster than 29.65%, Memory Usage: less than 41.48%

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''.join(e for e in s if e.isalnum()).lower()
        return newS == newS[::-1]