# 2022.09.29
# First Trial
# Time Limit Exceeded (20/21)

class MedianFinder:

    def __init__(self):
        self.arr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2 == 1:
            return self.arr[self.length // 2]
        else:
            return (self.arr[self.length // 2] + self.arr[self.length // 2 - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()