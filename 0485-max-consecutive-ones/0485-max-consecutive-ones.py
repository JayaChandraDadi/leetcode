class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        ct = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i]==1:
                ct+=1
            else:
                maxi = max(maxi,ct)
                ct=0
        return max(ct,maxi)