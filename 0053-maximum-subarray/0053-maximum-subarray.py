class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        sum1 = 0
        maxi = float('-inf')
        for i in range(n):
            sum1+=nums[i]
            maxi = max(maxi,sum1)
            if sum1<0:
                sum1  = 0
        return maxi