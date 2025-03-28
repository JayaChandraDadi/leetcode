class Solution(object):
    def majorityElement(self, nums):
        ct = 0
        el = -1
        for i in range(len(nums)):
            if ct==0:
                el = nums[i]
                ct+=1
            elif el==nums[i]:
                ct+=1
            else:
                ct-=1
        return el
        