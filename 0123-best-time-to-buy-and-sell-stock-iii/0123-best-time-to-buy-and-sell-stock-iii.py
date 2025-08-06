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
       after = [[0]*(3) for _ in range(2)]
       temp = after
       for i in range(n-1,-1,-1):
        for buy in range(1,-1,-1):
            for cap in range(2,0,-1):
                if buy==1:
                    temp[buy][cap] = max(-prices[i]+after[0][cap],after[1][cap])
                else:
                    temp[buy][cap] = max(prices[i]+after[1][cap-1],after[0][cap])
        after = temp
       return after[1][2]
       
       