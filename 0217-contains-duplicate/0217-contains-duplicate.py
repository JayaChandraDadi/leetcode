class Solution(object):
    def containsDuplicate(self, nums):
       if len(nums)==1:
        return False
       if len(set(nums))==len(nums):
        return False
       else:
        return True

        