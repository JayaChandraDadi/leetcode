class Solution(object):
    def canJump(self, nums):
       maxind = 0
       for i in range(len(nums)):
        if i>maxind:
            return False
        maxind = max(maxind,i+nums[i])
       return True