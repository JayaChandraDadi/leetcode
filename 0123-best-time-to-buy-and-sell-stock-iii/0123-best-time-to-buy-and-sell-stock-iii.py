class Solution:
    def profit(self,i,buy,transactions,prices,n,dp):
        if i==n or transactions==2:
            return 0
        if dp[i][buy][transactions]!=-1:
            return dp[i][buy][transactions]
        if buy==1:
            dp[i][buy][transactions] = max(-prices[i] + self.profit(i+1,0,transactions,prices,n,dp),self.profit(i+1,1,transactions,prices,n,dp))
        else:
            dp[i][buy][transactions] = max(prices[i] + self.profit(i+1,1,transactions+1,prices,n,dp),self.profit(i+1,0,transactions,prices,n,dp))
        return dp[i][buy][transactions]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*(3) for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for buy in range(2):
                for transactions in range(2):
                    if buy==1:
                        dp[i][buy][transactions] = max(-prices[i] + dp[i+1][0][transactions],dp[i+1][1][transactions])
                    else:
                        dp[i][buy][transactions] = max(prices[i] + dp[i+1][1][transactions+1],dp[i+1][0][transactions])
        return dp[0][1][0]