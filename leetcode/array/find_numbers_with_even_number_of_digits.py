class Solution(object):
# First trial (runtime: 35ms, memory usage: 13.4MB)
    def findNumbers(self, nums):
        even = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even += 1
        return even
        
# ---------------------------------------------------------------------------------------------
# Second trial (runtime: 54ms, memory usage: 13.3MB)
    def checkEvenStrnum(self, num):
        if len(str(num)) % 2 == 0:
            return 1
        else:
            return 0
        
    def findNumbers(self, nums):
        even = reduce(lambda x, y: x+y, map(self.checkEvenStrnum, nums))
        return even


# ---------------------------------------------------------------------------------------------
# Third trial refer to other's solution (runtime: 36ms, memory usage: 13.5MB)
    def checkEvenStrnum(self, num):
        return len([x for x in nums if len(str(x)) % 2 == 0])