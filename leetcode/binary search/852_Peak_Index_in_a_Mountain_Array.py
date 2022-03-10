class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # 2022-03-07

        # First Trial 

        # Time Complexity: O(log n) /   Runtime: faster than 99.63%
        # Space Complexity: O(1) /   Memory Usage: less than 15.74% 
        
        n = len(arr)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_right = arr[mid + 1]
            mid_left = arr[mid - 1]
            if mid == n - 1:
                mid_right = 0
            if mid == 0:
                mid_left = 0
            if arr[mid] > mid_left and arr[mid] > mid_right:
                return mid
            if mid_left > arr[mid]:
                right = mid - 1
            elif mid_right > arr[mid]:
                left = mid + 1
                