# 2022.09.29
# First Trial
# Time Limit Exceeded

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [[strs[0]]]
        
        def isAnagram(str1, str2):
            if len(str1) != len(str2):
                return False
            
            strDict = defaultdict(int)
            for s in str1:
                strDict[s] += 1
            for s in str2:
                if s not in strDict or strDict[s] == 0:
                    return False
                strDict[s] -= 1
            return True
        
        for i in range(1, len(strs)):
            for group in ans:
                if isAnagram(group[0], strs[i]):
                    group.append(strs[i])
                    break
            else:
                ans.append([strs[i]])
        
        return ans


# =================================================================
# Other's Solution
# Shortest
# Runtime: faster than 27.09%, Memory Usage: less than 54.22%

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        
        for word in strs:
            dict[tuple(sorted(word))].append(word)
            
        return list(dict.values())