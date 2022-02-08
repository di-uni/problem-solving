class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # First trial
        # Wrong answer (only consider specific cases)

        min_count = float("inf")
        coins.sort()
        
        for coin in range(len(coins) - 1, -1, -1):
            count = 0
            temp = amount

            for i in range(coin, -1, -1):
                count += temp // coins[i]
                temp = temp % coins[i]
                if temp == 0:
                    min_count = min(min_count, count)
                    continue
        
        if min_count == float("inf"):
            return -1
        else:
            return min_count

    # -----------------------------------------------------------------
        # Second trial
        # Time Limit Exceeded (15/188)

    def __init__(self):
        self.memo = {}
        self.minCount = float("inf")
        
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        self.memo[amount] = 0
        
        def dp(n):
            for coin in coins:
                if n > coin:
                    if n-coin not in self.memo:
                        self.memo[n - coin] = self.memo[n] + 1
                    else:
                        self.memo[n - coin] = min(self.memo[n - coin], self.memo[n] + 1)
                elif n == coin:
                    self.minCount = min(self.minCount, self.memo[n] + 1)
                    # print(self.minCount, self.memo[n] + 1)
                else:
                    continue
                dp(n - coin)
        
        dp(amount)
        # print(self.memo)
        if self.minCount == float("inf"):
            return -1
        return self.minCount