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
       dp = [[[-1]*(3) for _ in range(2)]for _ in range(n)]
       return self.profit(0,n,prices,1,2,dp)
        