class Solution:
    def dfs(self,i,buy,prices,dp):
        if i==len(prices):
            return 0
        if dp[i][buy]!=-1:
            return dp[i][buy]
        if buy==1:
            dp[i][buy] = max(-prices[i] + self.dfs(i+1,0,prices,dp),self.dfs(i+1,1,prices,dp))
        else:
            dp[i][buy] = max(prices[i]+self.dfs(i+1,1,prices,dp),self.dfs(i+1,0,prices,dp))
        return dp[i][buy]
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1]*(2) for _ in range(len(prices))]
        return self.dfs(0,1,prices,dp)