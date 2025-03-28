class Solution(object):
    def twoSum(self, nums, target):
       hashmap = {}
       for i in range(len(nums)):
        rem = target-nums[i]
        if rem in hashmap:
            return [hashmap[rem],i]
        else:
            hashmap[nums[i]] = i
    