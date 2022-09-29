# 2022.09.29
# First Trial
# Test Passed 
# Runtime: faster than 94.79%, Memory Usage: less than 67.03%

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        
        for e in s:
            s_dict[e] += 1
        
        for e in t:
            if e not in s_dict or s_dict[e] == 0:
                return False
            s_dict[e] -= 1
        
        return True



# =================================================================
# Other's Solution
# Shortest
# Runtime: faster than 23.32%, Memory Usage: less than 11.65%

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)