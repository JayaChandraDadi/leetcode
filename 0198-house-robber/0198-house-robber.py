class Solution(object):
    def rob(self, nums):
        n = len(nums)
        dp = [-1]*n
        dp[0] = nums[0]
        for i in range(1,n):
            if i-2<0:
                take = nums[i]
            else:
                take = nums[i] + dp[i-2]
            nottake = dp[i-1]
            dp[i] = max(take,nottake)
        return dp[n-1]
        