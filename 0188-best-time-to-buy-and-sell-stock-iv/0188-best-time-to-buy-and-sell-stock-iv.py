class Solution(object):
    def profit(self,i,n,prices,k,buy,dp):
        if k==0:
            return 0
        if i==n:
            return 0
        if dp[i][buy][k]!=-1:
            return dp[i][buy][k]
        if buy==1:
            dp[i][buy][k] = max(-prices[i]+self.profit(i+1,n,prices,k,0,dp),self.profit(i+1,n,prices,k,1,dp))
        else:
            dp[i][buy][k] = max(prices[i]+self.profit(i+1,n,prices,k-1,1,dp),self.profit(i+1,n,prices,k,0,dp))
        return dp[i][buy][k]
    def maxProfit(self, k, prices):
        n = len(prices)
        dp = [[[-1]*(k+1) for _ in range(2)] for _ in range(n)]
        return self.profit(0,n,prices,k,1,dp)