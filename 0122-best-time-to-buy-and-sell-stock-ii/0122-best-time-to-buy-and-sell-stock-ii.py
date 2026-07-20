class Solution:
    def profit(self,i,buy,prices,dp):
        if i==len(prices):
            return 0
        if dp[i][buy]!=-1:
            return dp[i][buy]
        if buy==1:
            dp[i][buy] = max(-prices[i] + self.profit(i+1,0,prices,dp),self.profit(i+1,1,prices,dp))
        else:
            dp[i][buy] = max(prices[i] + self.profit(i+1,1,prices,dp),self.profit(i+1,0,prices,dp))
        return dp[i][buy]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prev = [0]*(2)
        for i in range(len(prices)-1,-1,-1):
            curr = [0]*(2)
            for buy in range(2):
                if buy==1:
                    curr[buy] = max(-prices[i] + prev[0],prev[1])
                else:
                    curr[buy] = max(prices[i] + prev[1],prev[0])
            prev = curr
        return prev[1]
