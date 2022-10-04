# 2022.10.04
# First Trial
# Test Passed 
# Runtime: faster than 17.36%, Memory Usage: less than 27.16%

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = nums[0]
        
        for i in range(len(nums)-1):
            res[i+1] = res[i] + nums[i+1]
            
        return res


# =================================================================
# Other's Solution
# Shortest
# Runtime: faster than 14.87%, Memory Usage: less than 27.16%

from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)