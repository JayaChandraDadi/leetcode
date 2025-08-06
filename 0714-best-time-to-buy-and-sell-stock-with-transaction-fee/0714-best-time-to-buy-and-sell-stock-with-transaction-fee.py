class Solution(object):
    def profit(self,i,n,prices,fee,buy,dp):
        if i==n:
            return 0
        if dp[i][buy]!=-1:
            return dp[i][buy]
        if buy==1:
            dp[i][buy] = max(-prices[i]+self.profit(i+1,n,prices,fee,0,dp),self.profit(i+1,n,prices,fee,1,dp))
        else:
            dp[i][buy] = max(prices[i]-fee+self.profit(i+1,n,prices,fee,1,dp),self.profit(i+1,n,prices,fee,0,dp))
        return dp[i][buy]
    def maxProfit(self, prices, fee):
        n = len(prices)
        dp = [[-1]*(2) for _ in range(n)]
        return self.profit(0,n,prices,fee,1,dp)
        