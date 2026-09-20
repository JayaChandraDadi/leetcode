class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[-1]*(2) for _ in range(len(prices))]
        def profit(i,buy):
            if i==len(prices):
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy==1:
                dp[i][buy] = max(-prices[i] + profit(i+1,0),profit(i+1,1))
            else:
                dp[i][buy] = max(prices[i] + profit(i+1,1),profit(i+1,0))
            return dp[i][buy]
        return profit(0,1)