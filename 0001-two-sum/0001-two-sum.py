class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        i = 0
        for i in range(n):
            for j in range(i+1,n):
                sum1=nums[j]+nums[i]
                if sum1==target:
                    return [i,j]
