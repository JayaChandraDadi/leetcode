class Solution(object):
    def missingNumber(self, nums):
        xor = 0
        xor1 = 0
        for i in range(len(nums)):
            xor = xor^nums[i]
            xor1 = xor1^(i+1)
        return xor^xor1
        