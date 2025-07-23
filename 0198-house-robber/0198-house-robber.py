class Solution(object):
    def rob(self, nums):
        n = len(nums)
        prev1 = nums[0]
        prev2 = 0
        curri  = nums[0]
        for i in range(1,n):
            if i-2<0:
                take = nums[i]
            else:
                take = nums[i] + prev2
            nottake = prev1
            curri = max(take,nottake)
            prev2 = prev1
            prev1 = curri
        return curri
        