class Solution(object):
    def subarraySum(self, nums, k):
        sum1 = 0
        ct = 0
        n = len(nums)
        presummap = {}
        for i in range(n):
            sum1+=nums[i]
            if sum1==k:
                ct+=1
            rem = sum1-k
            if rem in presummap:
                ct+=presummap[rem]
            if sum1 not in presummap:
                presummap[sum1]=1
            else:
                presummap[sum1]+=1
        return ct