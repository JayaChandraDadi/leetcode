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
        dp = [[-1]*2 for _ in range(n)]
        return self.profit(0,1,len(prices),prices,dp)
        