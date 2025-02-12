class Solution(object):
    def subarraySum(self, nums, k):
        ct = 0
        sum1 = 0
        presummap = {}
        presummap[0] = 1
        rem = -3
        for i in range(len(nums)):
            sum1+=nums[i]
            rem = sum1-k
            if rem in presummap:
                ct+=presummap[rem]
            if sum1 not in presummap:
                presummap[sum1] =1
            else:
                presummap[sum1]+= 1
        return ct
        