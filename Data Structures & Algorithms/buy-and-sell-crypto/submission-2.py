class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for b in range(n):
            for s in range(b+1,n):
                profit = prices[s] - prices[b]
                max_profit = max(max_profit, profit)
            
        return max_profit