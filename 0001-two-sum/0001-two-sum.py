class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        sum1 = 0
        for i in range(len(nums)):
            sum1 = nums[i]
            if target-sum1 in hashmap:
                return [hashmap[target-sum1],i]
            hashmap[sum1] = i
