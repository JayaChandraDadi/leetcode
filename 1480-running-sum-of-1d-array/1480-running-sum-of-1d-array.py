class Solution(object):
    def runningSum(self, nums):
        sum1 = 0
        for i in range(len(nums)):
            sum1+=nums[i]
            nums[i] = sum1
        return nums