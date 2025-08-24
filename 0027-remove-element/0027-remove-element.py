class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            else:
                continue
        return i


        