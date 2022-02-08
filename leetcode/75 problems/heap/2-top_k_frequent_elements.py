import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # First trial
        # Error in test case: nums = [1, 2] k = 2

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
            
            