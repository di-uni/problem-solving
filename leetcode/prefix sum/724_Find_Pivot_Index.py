# 2022.10.04
# First Trial
# Test Passed 
# Runtime: faster than 11.20%, Memory Usage: less than 48.45%

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = 0
        suffixSum = sum(nums)
        
        for i, n in enumerate(nums):
            suffixSum -= n
            if prefixSum == suffixSum:
                return i
            prefixSum += n
            
        return -1


# =================================================================
# Other's Solution
# Calculate whether prefixSum * 2 + nums[i] == total or not
# Runtime: faster than 30.30%, Memory Usage: less than 48.45%

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum, total = 0, sum(nums)
        
        for i, n in enumerate(nums):
            if prefixSum * 2 + n == total:
                return i
            prefixSum += n
            
        return -1
        
        