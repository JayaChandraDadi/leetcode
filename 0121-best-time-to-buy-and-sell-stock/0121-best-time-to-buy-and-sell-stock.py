class Solution(object):
    def maxProfit(self, nums):
        min1 = nums[0]
        maxprofit = 0
        profit = 0
        for i in range(len(nums)):
            if nums[i]<min1:
                min1 = nums[i]
            profit = nums[i]-min1
            maxprofit = max(profit,maxprofit)
        return maxprofit
            


        