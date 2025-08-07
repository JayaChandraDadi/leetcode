class Solution(object):
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        dp = [1]*n
        hash = [0]*n
        maxi = 1
        index  = 0
        nums.sort()
        for i in range(n):
            hash[i] = i
            for prev in range(i):
                if nums[i]%nums[prev]==0 and dp[i]<dp[prev]+1:
                    dp[i] = dp[prev]+1
                    hash[i] = prev
            if dp[i]>maxi:
                maxi = dp[i]
                index = i
        ans = []
        ans.append(nums[index])
        while(hash[index]!=index):
            index = hash[index]
            ans.append(nums[index])
        return ans
        