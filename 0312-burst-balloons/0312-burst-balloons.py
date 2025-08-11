class Solution(object):
    def maximum(self,i,j,nums,dp):
        if i>j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        maxi = float('-inf')
        for ind in range(i,j+1):
            coins = (nums[i-1]*nums[ind]*nums[j+1]) + self.maximum(i,ind-1,nums,dp) + self.maximum(ind+1,j,nums,dp)
            maxi = max(maxi,coins)
        dp[i][j] = maxi
        return dp[i][j]
    def maxCoins(self, nums):
        nums.append(1)
        nums = [1] + nums
        n = len(nums)
        dp = [[0]*(n) for _ in range(n)]
        for i in range(n-2,0,-1):
            for j in range(i,n-1):
                maxi = float('-inf')
                for ind in range(i,j+1):
                    coins = (nums[i-1]*nums[ind]*nums[j+1]) + dp[i][ind-1] + dp[ind+1][j]
                    maxi = max(maxi,coins)
                dp[i][j] = maxi
        return dp[1][n-2]