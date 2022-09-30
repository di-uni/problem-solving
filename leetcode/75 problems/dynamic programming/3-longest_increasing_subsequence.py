# 2022.09.30
# First Trial
# Test Passed 
# Runtime: faster than 64.19%, Memory Usage: less than 13.08%

from bisect import bisect_left
from collections import defaultdict
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dict = defaultdict(list)
        dict[1].append(nums[0])
        max_sub = 1
        
        for n in range(1, len(nums)):
            num = nums[n]
            # print("num:", num)
            for i in range(max_sub, 0, -1):
                if i not in dict or num > min(dict[i]):
                    dict[i+1].append(num)
                    max_sub = max(max_sub, i+1)
                    # print(dict)
                    break
            else:
                dict[1].append(num)
        # print(dict) 
        
        return max_sub



# =================================================================
# Other's Solution (1)
# Using dp
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)

# Runtime: faster than 61.77%, Memory Usage: less than 82.40%

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                # print(i, j, nums[i], nums[j], dp)
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        
        return max(dp) 


# Other's Solution (2)
# Using bisect
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)

# Runtime: faster than 79.04%, Memory Usage: less than 46.09%

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                # Find the index of the smallest number >= x
                idx = bisect_left(sub, x)
                sub[idx] = x
        return len(sub)