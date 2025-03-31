class Solution(object):
    def subset(self,nums,i,stack,res,n):
        if i==n:
            if stack not in res:
                res.append(stack[:])
            return
        stack.append(nums[i])
        self.subset(nums,i+1,stack,res,n)
        stack.pop()
        self.subset(nums,i+1,stack,res,n)
    def subsetsWithDup(self, nums):
        n = len(nums)
        nums.sort()
        stack = []
        res = []
        self.subset(nums,0,stack,res,n)
        return res
        