class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return
