class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                return True
        return False