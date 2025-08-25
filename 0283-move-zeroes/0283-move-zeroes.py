class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i]==0:
                break
        for j in range(i+1,n):
            if nums[j]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        

        