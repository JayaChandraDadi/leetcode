class Solution(object):
    def findDuplicate(self, nums):
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return nums[i]
            hashmap[nums[i]] = 1
        
        