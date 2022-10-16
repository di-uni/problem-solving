# 2022.10.15
# First Trial
# Time Limit Exceeded

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(s) < len(p): return ans
        
        sorted_p = sorted(p)
        for i in range(len(s)):
            sub_s = sorted(s[i:i + len(p)])
            if sub_s == sorted_p:
                ans.append(i)
        
        return ans


# Second Trial referred to discussion
# Test Passed
# Runtime: faster than 69.94%, Memory Usage: less than 81.98%

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(s) < len(p): return ans
        
        p_cnt = [0] * 26
        s_cnt = [0] * 26
        
        for i in range(len(p)):
            p_cnt[ord(p[i]) - 97] += 1
            s_cnt[ord(s[i]) - 97] += 1
        
        for i in range(len(p), len(s)):
            # print(i, i - len(p))
            # print(p_cnt, s_cnt)
            if p_cnt == s_cnt:
                ans.append(i - len(p))
            to_remove, last = s[i - len(p)], s[i]
            s_cnt[ord(to_remove) - 97] -= 1
            s_cnt[ord(last) - 97] += 1
            
        if p_cnt == s_cnt:
            ans.append(len(s) - len(p))
        
        return ans
            
            
            