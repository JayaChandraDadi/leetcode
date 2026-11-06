class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = 1
        n = len(nums)
        prefix = [1]*n
        for i in range(n):
            prefix[i] = product
            product = product*nums[i]
        product = 1
        suffix = [1]*n
        for i in range(n-1,-1,-1):
            suffix[i] = product
            product = product*nums[i]
        ans = [1]*n
        for i in range(n):
            ans[i] = prefix[i]*suffix[i]
        return ans