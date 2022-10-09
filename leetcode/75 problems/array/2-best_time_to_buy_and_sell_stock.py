# First trial 
# Time Limit Exceeded

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for i in range(len(prices)-1):
            for j in range(i + 1, len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        return max(maxProfit, 0)
                

# 2022.10.08
# Second Trial
# Test Passed
# Runtime: faster than 74.33%, Memory Usage: less than 7.00%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = maxVal = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            # print(maxVal, minVal)
            if prices[i] < minVal:
                maxProfit = max(maxProfit, maxVal - minVal)
                minVal = maxVal = prices[i]
                continue
            maxVal = max(maxVal, prices[i])
        
        return max(maxProfit, maxVal - minVal)




# =================================================================
# Other's Solution
# Clean code
# Runtime: faster than 15.34%, Memory Usage: less than 7.00%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, minPrice = 0, float("inf")
        for price in prices:
            minPrice = min(price, minPrice)
            profit = price - minPrice
            maxProfit = max(profit, maxProfit)
            
        return maxProfit