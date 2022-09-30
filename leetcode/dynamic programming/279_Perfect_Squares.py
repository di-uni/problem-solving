# 2022.09.30
# First Trial
# Time Limit Exceeded (502/588)

from heapq import heappush, heappop

class Solution:
    def numSquares(self, n: int) -> int:
        perfectSquares = []
        for i in range(1, int(n**(1/2)) + 1):
            perfectSquares.append(i**2)
        
        # print("**", n, perfectSquares)
        
        dict = {}
        heap = []
        heappush(heap, (0, 0))
        
        while heap:
            curNum, curSum = heappop(heap)
            if curSum in dict:
                continue
            dict[curSum] = curNum
            # print(curNum, curSum)
            if -curSum == n:
                return curNum
            for pq in perfectSquares:
                if -curSum + pq > n:
                    continue
                if (curNum+1, curSum-pq) not in heap:
                    heappush(heap, (curNum+1, curSum-pq))
            # print(heap)


# =================================================================
# Other's Solution
# Using set
# https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS

# Runtime: faster than 74.85%, Memory Usage: less than 31.42%

class Solution:
    def numSquares(self, n: int) -> int:
        perfectSquares = []
        for i in range(1, int(n**(1/2)) + 1):
            perfectSquares.append(i**2)
        
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                # print(x)
                for ps in perfectSquares:
                    if x == ps:
                        return cnt
                    if x < ps:
                        break
                    temp.add(x-ps)
                # print(temp)
            toCheck = temp
        
        return cnt
            