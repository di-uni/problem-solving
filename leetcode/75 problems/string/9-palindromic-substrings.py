# 2022.09.29
# First Trial
# Test Passed 
# Runtime: faster than 5.36%, Memory Usage: less than 26.46%

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        def isPalindrome(st):
            return st == st[::-1]
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    ans += 1
        
        return ans


# =================================================================
# Other's Solution
# O(1): from middle to two ends

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''

        # get the longest palindrome, l, r are the middle indexes
        # from inner to outer
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # odd case, like "aba"
            tmp = helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res