# 2022.09.29
# First Trial
# Test Passed 
# Runtime: faster than 7.20%, Memory Usage: less than 49.77%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_num = 0

        for i in range(len(s)):
            char_dict = {}
            cur_num = 0
            for j in range(i, len(s)):
                if s[j] in char_dict:
                    break
                char_dict[s[j]] = 1
                cur_num += 1
            max_num = max(max_num, cur_num)
            
        return max_num


# =================================================================
# Other's Solution
# O(1)
# Runtime: faster than 99.85%, Memory Usage: less than 49.77%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i-start+1)
            usedChar[s[i]] = i
        
        return maxLength