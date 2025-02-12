class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max1 = 0
        ct = 0
        for i in range(len(nums)):
            if nums[i]==1:
                ct+=1
                max1 = max(max1,ct)
            else:
                ct = 0
        return max1
            
        