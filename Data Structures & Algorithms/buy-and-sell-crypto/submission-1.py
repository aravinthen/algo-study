class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i1 = 0
        i2 = 1

        n = len(prices)
        if n == 1:
            return 0
        
        max_profit = 0
        while i2 < n:
            if prices[i1] < prices[i2]:
                profit = prices[i2] - prices[i1]
                max_profit = max(max_profit, profit)
            else:
                i1=i2
            i2 += 1
            
        return max_profit