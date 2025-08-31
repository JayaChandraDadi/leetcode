class Solution(object):
    def productExceptSelf(self, nums):
        prefix = 1
        n = len(nums)
        output = [0]*(n)
        for i in range(n):
            output[i] = prefix
            prefix = prefix*nums[i]
        postfix = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i]*postfix
            postfix = postfix*(nums[i])
        return output