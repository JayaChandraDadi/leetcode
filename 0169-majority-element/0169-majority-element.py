class Solution(object):
    def majorityElement(self, nums):
        ct = 0
        n = len(nums)
        for i in range(n):
            if ct==0:
                el = nums[i]
                ct+=1
            elif el==nums[i]:
                ct+=1
            else:
                ct-=1
        return el