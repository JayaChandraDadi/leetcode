class Solution(object):
    def maxProfit(self, nums):
        buy = nums[0]
        maxprofit = 0
        for i in range(1,len(nums)):
            maxprofit = max(maxprofit,nums[i]-buy)
            buy = min(buy,nums[i])
        return maxprofit
        