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
        front1 = [0]*(2)
        front2 = [0]*(2)
        for i in range(n-1,-1,-1):
            temp = [0] * 2
            for buy in range(1,-1,-1):
                if buy==1:
                    temp[buy] = max(-prices[i]+front1[0],front1[1])
                else:
                    temp[buy] = max(prices[i]+front2[1],front1[0])
            front2 = front1
            front1 = temp
        return temp[1]
