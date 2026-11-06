class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[-1]*(2) for _ in range(len(prices))]
        def profit(i,buy,nums,dp):
            if i==len(nums):
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy==1:
                dp[i][buy] = max(-nums[i] + profit(i+1,0,nums,dp),profit(i+1,1,nums,dp))
            else:
                dp[i][buy] = max(nums[i] + profit(i+1,1,nums,dp),profit(i+1,0,nums,dp))
            return dp[i][buy]
        return profit(0,1,prices,dp)