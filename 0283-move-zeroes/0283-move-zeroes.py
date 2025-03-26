class Solution(object):
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i]==0:
                break
        for j in range(i+1,len(nums)):
            if nums[i]!=nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        
