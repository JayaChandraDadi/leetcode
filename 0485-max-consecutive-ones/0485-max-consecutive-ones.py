class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi = float('-inf')
        ct = 0
        for i in range(len(nums)):
            if nums[i]==1:
                ct+=1
            else:
                maxi = max(maxi,ct)
                ct = 0
        return max(maxi,ct)

