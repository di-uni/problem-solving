# 2022.09.29
# First Trial
# Time Limit Exceeded

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        
        def maxCharCnt(s):
            dict = defaultdict(int)
            for e in s:
                dict[e] += 1
            return max(dict.values())
        
        for i in range(len(s)):
            for j in range(i+k, len(s)):
                if j-i+1 <= maxCharCnt(s[i:j+1]) + k:
                    maxLen = max(maxLen, j-i+1)
                # print(s[i:j+1], maxCharCnt(s[i:j+1]))
        
        return maxLen



# =================================================================
# Other's Solution
# Using Counter
# Runtime: faster than 59.13%, Memory Usage: less than 57.12% 

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = res = 0      # maxf: max frequency, res: longest length result
        count = Counter()
        
        for i in range(len(s)):
            count[s[i]] += 1
            maxf = max(maxf, count[s[i]])
            if res - maxf < k:
                res += 1
            else:
                count[s[i - res]] -= 1
            # print(count, res, maxf)
            
        return res