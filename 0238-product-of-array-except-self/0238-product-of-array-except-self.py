class Solution(object):
    def productExceptSelf(self, nums):
        prefix = 1
        ans = []
        for i in range(len(nums)):
            ans.append(prefix)
            prefix = prefix*nums[i]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i]*suffix
            suffix = suffix*nums[i]
        return ans