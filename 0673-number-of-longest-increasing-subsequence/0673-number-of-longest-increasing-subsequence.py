class Solution(object):
    def findNumberOfLIS(self, nums):
        n = len(nums)
        dp = [1]*n
        ct = [1]*n
        maxi = 0
        nos = 0
        for i in range(n):
            for prev in range(i):
                if nums[prev]<nums[i] and dp[i]<dp[prev]+1:
                    dp[i] = dp[prev]+1
                    ct[i] = ct[prev]
                elif nums[prev]<nums[i] and dp[i]==dp[prev]+1:
                    ct[i]+=ct[prev]
            if maxi<dp[i]:
                maxi = dp[i]
        for i in range(n):
            if maxi==dp[i]:
                nos+=ct[i]
        return nos
        