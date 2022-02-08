class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        # prevOne = 0
        # maxConsecutiveOne = 0
        # consecutiveOne = 0
        
        # First trial with for loop 

        # Runtime: 371ms (27.73%), 
        # Memory usage: 13.7MB (53.74%)
        
        for num in nums:
            if num == 1:
                consecutiveOne += 1
                if prevOne == 0:
                    prevOne = 1
            else:
                if prevOne == 1:
                    if maxConsecutiveOne < consecutiveOne:
                        maxConsecutiveOne = consecutiveOne
                    prevOne = 0
                    consecutiveOne = 0
        if maxConsecutiveOne < consecutiveOne:
            maxConsecutiveOne = consecutiveOne
        return maxConsecutiveOne
        

        # -----------------------------------------------
        # Second trial
        
        prevZero = -1
        for i in range(len(nums)):
            # print("i = ", i)
            if nums[i] == 1:
                if prevOne == 0:
                    prevOne = 1
            else:
                if prevOne == 1:
                    consecutiveOne = i - prevZero - 1
                    # print(prevZero, consecutiveOne, i)
                    if maxConsecutiveOne < consecutiveOne:
                        maxConsecutiveOne = consecutiveOne
                    prevOne = 0
                    consecutiveOne = 0
                prevZero = i
        if prevOne == 1:
            consecutiveOne = i - prevZero
            # print(prevZero, consecutiveOne, i)
            if maxConsecutiveOne < consecutiveOne:
                maxConsecutiveOne = consecutiveOne
        return maxConsecutiveOne


        # -----------------------------------------------
        # Third trial refer to other's solution 
        # Runtime: 288ms (85.61%)
        # Memory usage: 13.6MB (72.17%)
        
        maxConsecutiveOne = 0
        consecutiveOne = 0
        
        for num in nums:
            if num == 1:
                consecutiveOne += 1
            else:
                maxConsecutiveOne = max(maxConsecutiveOne, consecutiveOne)
                consecutiveOne = 0
        return max(maxConsecutiveOne, consecutiveOne)