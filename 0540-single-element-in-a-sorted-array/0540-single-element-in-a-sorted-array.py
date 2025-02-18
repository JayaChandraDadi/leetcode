class Solution(object):
    def singleNonDuplicate(self, nums):
        xor1 = 0
        for i in range(len(nums)):
            xor1 = xor1^nums[i]
        return xor1
        