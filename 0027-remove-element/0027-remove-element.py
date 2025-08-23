class Solution(object):
    def removeElement(self, nums, val):
        temp = []
        for i in range(len(nums)):
            if nums[i]!=val:
                temp.append(nums[i])
        for i in range(len(temp)):
           nums[i] = temp[i]
        return len(temp)