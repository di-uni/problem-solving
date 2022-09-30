# 2022.09.30
# First Trial
# Using bfs with heap
# Test Passed 
# Runtime: faster than 29.72%, Memory Usage: less than 26.61%

from heapq import heappush, heappop
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        maxNum = -1
    
        heap = []
        heappush(heap, (0, 0))
        coinSumDict = {}
        
        while heap:
            coinCnt, coinSum = heappop(heap)
            
            if coinSum in coinSumDict:
                continue
            coinSumDict[coinSum] = coinCnt
            
            if coinSum == amount:
                maxNum = max(maxNum, coinCnt)
                return coinCnt
            if coinSum > amount:
                continue
            for coin in coins:
                heappush(heap, (coinCnt + 1, coinSum - coin))
            
        return maxNum



# =================================================================
# Other's Solution
# Using dp
# Runtime: faster than 57.60%, Memory Usage: less than 40.43% 

from heapq import heappush, heappop
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[-1] == float('inf'):
            return -1
    
        return dp[-1]