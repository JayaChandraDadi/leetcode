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
        dp = [[[0]*(k+1) for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(k,0,-1):
                    if buy==1:
                        dp[i][buy][cap] = max(-prices[i]+dp[i+1][0][cap],dp[i+1][1][cap])
                    else:
                        dp[i][buy][cap] = max(prices[i]+dp[i+1][1][cap-1],dp[i+1][0][cap])
        return dp[0][1][k]
        
