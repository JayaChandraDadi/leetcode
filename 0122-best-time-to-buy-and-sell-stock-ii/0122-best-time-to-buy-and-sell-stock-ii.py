class Solution(object):
    def profit(self,i,buy,n,prices,dp):
        if i==n:
            return 0
        if dp[i][buy]!=-1:
            return dp[i][buy]
        if buy==1:
            dp[i][buy] = max(-prices[i]+self.profit(i+1,0,n,prices,dp),self.profit(i+1,1,n,prices,dp))
        else:
            dp[i][buy] = max(prices[i]+self.profit(i+1,1,n,prices,dp),self.profit(i+1,0,n,prices,dp))
        return dp[i][buy]
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        dp[n][0] = 0
        dp[n][1] = 0
        for i in range(n-1,-1,-1):
            for buy in range(2):
                profit = 0
                if buy==1:
                    profit = max(-prices[i]+dp[i+1][0],dp[i+1][1])
                else:
                    profit = max(prices[i]+dp[i+1][1],dp[i+1][0])
                dp[i][buy] = profit
        return profit

        