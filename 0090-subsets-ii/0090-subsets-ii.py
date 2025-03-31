class Solution(object):
    def subset(self,nums,i,stack,res,n):
        res.append(stack[:])
        for j in range(i,n):
            if j>i and nums[j]==nums[j-1]:
                continue
            stack.append(nums[j])
            self.subset(nums,j+1,stack,res,n)
            stack.pop()
    def subsetsWithDup(self, nums):
        n = len(nums)
        nums.sort()
        stack = []
        res = []
        self.subset(nums,0,stack,res,n)
        return res
        