class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            rem = target - nums[i]
            if rem in hashmap:
                return [hashmap[rem],i]
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i