class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # First trial

        # Time Complexity: O(n^2) /   Runtime: faster than 50.10%
        # Space Complexity: O(n) /   Memory Usage: less than 18.78%

        s = 0
        d = 0
        
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n != 0:
            for i in range(n + m):
                if nums1[i] >= nums2[d]:
                    for j in range(n + m - 1, i, -1):
                        nums1[j] = nums1[j-1]
                    nums1[i] = nums2[d]
                    d += 1
                    if d == n:
                        break
                else:
                    s += 1
                # print(nums1[i], d, s)
                if s > m and nums1[i] == 0:
                    nums1[i] = nums2[d]
                    d += 1
        
    # -----------------------------------------------------------------
