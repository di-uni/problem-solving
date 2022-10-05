# 2022.10.05
# First Trial
# Test Passed 
# Runtime: faster than 29.13%, Memory Usage: less than 42.75%

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == 0: return True
        
        i = 0
        for c in t:
            if s[i] == c:
                i += 1
                if i >= len(s):
                    return True
        return False


# =================================================================
# Other's Solution (1)
# Concise
# Runtime: faster than 17.28%, Memory Usage: less than 81.89%

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
    
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)


# Other's Solution (2)
# Using binary search
# Runtime: faster than 17.28%, Memory Usage: less than 81.89%

from collections import defaultdict
from bisect import bisect_left

class Solution(object):
    def createMap(self, s: str):
        posMap = defaultdict(list)
        for i, char in enumerate(s):
            posMap[char].append(i)
        return posMap
    
    def isSubsequence(self, s: str, t: str) -> bool:
        posMap = self.createMap(t)
        lowBound = 0
        
        for char in s:
            if char not in posMap: return False
            charIndexList = posMap[char]
            i = bisect_left(charIndexList, lowBound)
            if i == len(charIndexList): return False
            lowBound = charIndexList[i] + 1
        return True