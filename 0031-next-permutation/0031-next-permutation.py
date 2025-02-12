class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        pt = -1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pt = i
                break
        if pt==-1:
            nums.reverse()
            return nums
        for i in range(n-1,pt,-1):
            if nums[i]>nums[pt]:
                nums[pt],nums[i] = nums[i],nums[pt]
                break
        nums[pt+1:] = reversed(nums[pt+1:])
        return nums

        