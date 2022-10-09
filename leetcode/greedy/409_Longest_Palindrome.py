# 2022.10.08
# First Trial
# Test Passed
# Runtime: faster than 82.50%, Memory Usage: less than 22.72%

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        char_cnt = Counter(s)
        add_center = False
        
        for num in char_cnt.values():
            if not add_center and num % 2 == 1:
                res += 1
                add_center = True
            res += (num // 2) * 2
            
        return res



# =================================================================
# Other's Solution (1)
# Using 비트연산 (보수)
# Runtime: faster than 94.79%, Memory Usage: less than 66.71%

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # v & ~1: 홀수만 1 빼줌 (보수 연산)
        use = sum(v & ~1 for v in Counter(s).values())
        return use + (use < len(s))



# Other's Solution (2)
# Using set
# Runtime: faster than 35.00%, Memory Usage: less than 97.31%

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)