class Solution(object):
    def maxSubArray(self, nums):
        maxsum = float("-inf")
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            maxsum = max(maxsum,sum)
            if sum<0:
                sum = 0
        return maxsum
