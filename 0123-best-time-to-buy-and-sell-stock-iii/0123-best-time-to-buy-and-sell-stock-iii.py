class Solution(object):
    def profit(self,i,n,prices,buy,cap,dp):
        if i==n:
            return 0
        if cap==0:
            return 0
        if dp[i][buy][cap]!=-1:
            return dp[i][buy][cap]
        if buy==1:
            dp[i][buy][cap] = max(-prices[i]+self.profit(i+1,n,prices,0,cap,dp),self.profit(i+1,n,prices,1,cap,dp))
        else:
            dp[i][buy][cap] = max(prices[i]+self.profit(i+1,n,prices,1,cap-1,dp),self.profit(i+1,n,prices,0,cap,dp))
        return dp[i][buy][cap]
    def maxProfit(self, prices):
       n = len(prices)
       dp = [[[-1]*(3) for _ in range(2)]for _ in range(n+1)]
       for i in range(n+1):
        for buy in range(2):
            dp[i][buy][0] = 0
       for buy in range(2):
        for cap in range(3):
            dp[n][buy][cap] = 0
       for i in range(n-1,-1,-1):
        for buy in range(1,-1,-1):
            for cap in range(2,0,-1):
                if buy==1:
                    dp[i][buy][cap] = max(-prices[i]+dp[i+1][0][cap],dp[i+1][1][cap])
                else:
                    dp[i][buy][cap] = max(prices[i]+dp[i+1][1][cap-1],dp[i+1][0][cap])
       return dp[0][1][2]
       
       