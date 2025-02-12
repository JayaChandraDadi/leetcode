class Solution(object):
    def rearrangeArray(self, nums):
        pos = 0
        neg = 1
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                ans[pos] = nums[i]
                pos+=2
            else:
                ans[neg] = nums[i]
                neg+=2
        return ans
        