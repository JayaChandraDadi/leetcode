class Solution(object):
    def maxProfit(self, nums):
        buy = nums[0]
        maxprofit = 0
        for i in range(1,len(nums)):
            if nums[i]<buy:
                buy = nums[i]
            maxprofit = max(maxprofit,nums[i]-buy)
        return maxprofit
        