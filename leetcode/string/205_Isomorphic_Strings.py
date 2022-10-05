# 2022.10.05
# First Trial
# Test Passed 
# Runtime: faster than 95.48%, Memory Usage: less than 45.73%

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        
        for _s, _t in zip(s, t):
            if _s not in s2t and _t not in t2s:
                s2t[_s] = _t
                t2s[_t] = _s
            if _s in s2t and s2t[_s] != _t:
                return False
            if _t in t2s and t2s[_t] != _s:
                return False
                
        return True


# =================================================================
# Other's Solution
# Shortest
# Runtime: faster than 23.80%, Memory Usage: less than 88.55%

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))