class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = float('-inf')
        n = len(prices)
        for i in range(n):
            buy = min(buy,prices[i])
            profit = max(profit,prices[i]-buy)
        return profit