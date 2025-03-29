class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        res = []
        for num in range(1<<n):
            subset=[]
            for i in range(n):
                if num&(1<<i):
                    subset.append(nums[i])
            res.append(subset)
        return res
        