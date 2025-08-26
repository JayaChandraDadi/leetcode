class Solution(object):
    def maxProfit(self, nums):
        n = len(nums)
        buy = nums[0]
        maxprofit = 0
        for i in range(len(nums)):
            profit = nums[i]-buy
            maxprofit = max(maxprofit,profit)
            if nums[i]<buy:
                buy = nums[i]
        return maxprofit