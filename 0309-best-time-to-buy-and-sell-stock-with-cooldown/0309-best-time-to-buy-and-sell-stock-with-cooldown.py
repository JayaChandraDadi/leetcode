class Solution(object):
    def profit(self,i,n,prices,buy,dp):
        if i>=n:
            return 0
        if dp[i][buy]!=-1:
            return dp[i][buy]
        if buy==1:
            dp[i][buy] = max(-prices[i]+self.profit(i+1,n,prices,0,dp),self.profit(i+1,n,prices,1,dp))
        else:
            dp[i][buy] = max(prices[i]+self.profit(i+2,n,prices,1,dp),self.profit(i+1,n,prices,0,dp))
        return dp[i][buy]
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0]*(2) for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            for buy in range(1,-1,-1):
                if buy==1:
                    dp[i][buy] = max(-prices[i]+dp[i+1][0],dp[i+1][1])
                else:
                    dp[i][buy] = max(prices[i]+dp[i+2][1],dp[i+1][0])
        return dp[0][1]
