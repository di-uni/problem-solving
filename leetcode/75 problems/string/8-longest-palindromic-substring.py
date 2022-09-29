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
# Using dp
# Runtime: faster than 8.94%, Memory Usage: less than 20.80%

# example: "abcbaea"
#    a b c b a e a
# a  o
# b  x o
# c  x x o
# b  x o x o
# a  o x x x o
# e  x x x x x o
# a  x x x x o x o

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # print(i, j, s[i], s[j])
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                res += dp[i][j]
                # print(dp)
        return res



# Other's Solution (2)
# Runtime: faster than 82.51%, Memory Usage: less than 38.83%

# example: "abcbaea"
# a
# b
# c, bcb, abcba
# b
# a
# e, aea
# a
# 해당 원소를 중심으로 하는 parlindrome을 모두 찾는다.

class Solution:
    def countSubstrings(self, s: str) -> int:   
        n = len(s)
        ans = 0
        for center in range(2*n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                # from middle to bound
                ans += 1
                left -= 1
                right += 1
        
        return ans