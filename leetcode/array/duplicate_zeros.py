class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

        # First trial

        # Time Complexity: O(n^2) /   Runtime: faster than 14.95%
        # Space Complexity: O(n) /   Memory Usage: ..

        prev = -1
        zero_cnt = 0
        
        for i in range(len(arr)):
            if arr[i] == 0:
                if prev != 0:
                    zero_cnt += 1
                    if i == len(arr) - 1:
                        break
                    if arr[i + 1] != 0:
                        for j in range(len(arr) - 1, i + 1, -1):
                            arr[j] = arr[j - 1]
                        arr[i + 1] = 0
                        zero_cnt -= 1
                else:
                    if zero_cnt != 0:
                        zero_cnt += 1
            if arr[i] != 0 and prev == 0 and zero_cnt > 0:
                for j in range(min(len(arr), len(arr) - zero_cnt), i - 1, -1):
                    # print(j, j-zero_cnt)
                    arr[j] = arr[j - zero_cnt]
                for j in range(i, min(len(arr), i + zero_cnt)):
                    # print(j)
                    arr[j] = 0
                zero_cnt = 0
            prev = arr[i]
            print(arr, i, zero_cnt)

    # -----------------------------------------------------------------
