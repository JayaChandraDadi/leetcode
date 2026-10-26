class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set(nums)
        if len(hashmap)==len(nums):
            return False
        return True
