class Solution(object):
    def nextPermutation(self, nums):
        pt = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                pt = i
                break
        if pt == -1:
           nums.reverse()
        else:
            for i in range(len(nums)-1,-1,-1):
                if nums[i]>nums[pt]:
                    nums[i],nums[pt] = nums[pt],nums[i]
                    break
            nums[pt+1:] = reversed(nums[pt+1:])
        

        