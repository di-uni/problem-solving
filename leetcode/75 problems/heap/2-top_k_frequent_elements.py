# First Trial
# Test Failed (Error in test case: nums = [1, 2] k = 2)

import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        reverse_dict = {}
        ans = []
        
        for n in nums:
            if n not in dict:
                dict[n] = 0
            dict[n] += 1
        
        # only consider the unique frequence
        for key, val in dict.items():
            if val not in dict:
                reverse_dict[val] = 0
            reverse_dict[val] = key
        
        frequence = [-x for x in reverse_dict.keys()]
        heapq.heapify(frequence)
        
        i = 0
        while i < k:
            temp = -1 * heapq.heappop(frequence)
            print(i, temp)
            ans.append(reverse_dict[temp])
            i += 1
            
        
        return ans

# -----------------------------------------------------------------
# Second trial refer to DP lecture
# Bottom-up (Tabulation)

# Time Complexity: O(n + k log n) /   Runtime: faster than 98.29%
# Space Complexity: O(n) /   Memory Usage: less than 55.32%

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        reverse_dict = {}
        ans = []
        
        for n in nums:
            if n not in dict:
                dict[n] = 0
            dict[n] += 1
        
        values = [-x for x in set(dict.values())]
        heapq.heapify(values)
        # print(values)
        
        i = 0
        while i < k:
            largest = -1 * heapq.heappop(values)
            temp = [key for key, val in dict.items() if val == largest]
            i += len(temp)
            for t in temp:
                ans.append(t)
            # print(largest, temp, i)
        
        return ans
            

# Third Trial
# 2022.09.30
# Test Passed
# Runtime: faster than 37.32%, Memory Usage: less than 47.95%

from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1
        
        heap = []
        for num in dict:
            heappush(heap, (-dict[num], num))
        
        for i in range(k):
            cnt, num = heappop(heap)
            ans.append(num)
        
        return ans



# =================================================================
# Other's Solution
# Clean code, using Counter
# Runtime: faster than 49.53%, Memory Usage: less than 71.44%

from heapq import heapify, heappop
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        maxHeap = [[-freq, num] for num, freq in cnt.items()]
        heapify(maxHeap)
        
        ans = []
        for i in range(k):
            _, num = heappop(maxHeap)
            ans.append(num)
        
        return ans