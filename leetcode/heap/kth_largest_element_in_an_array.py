import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # First trial

        # Time Complexity: O(n + k log n) /   Runtime: faster than 20.01%
        # Space Complexity: O(n) /   Memory Usage: less than 53.34%

        minus_nums = [-x for x in nums]
        heapq.heapify(minus_nums)
        for i in range(k - 1):
            heapq.heappop(minus_nums)
        return -1 * heapq.heappop(minus_nums)
        