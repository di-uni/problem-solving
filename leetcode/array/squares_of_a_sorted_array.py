class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # First trial (not works in specific situation)

        fromBack = len(nums) - 1
        squares = []
        
        for i, n in enumerate(nums):
            if n <= 0:
                while(nums[fromBack]*nums[fromBack] > n*n):
                    squares.insert(0, nums[fromBack]*nums[fromBack])
                    fromBack -= 1
                    if fromBack == i:
                        break
                squares.insert(0, n*n)
            else:
                if fromBack + 1 == i:
                    break
                # squares.insert(0, n*n)
                squares.append(n*n)
        return squares


        # -----------------------------------------------
        # Second trial refer to other's solution

        deq = deque()
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left < right:
                deq.appendleft(nums[r]*nums[r])
                r -= 1
            else:
                deq.appendleft(nums[l]*nums[l])
                l += 1
        return deq


        # -----------------------------------------------
        # Third trial refer to other's solution (fastest)

        return sorted([n*n for n in nums])
