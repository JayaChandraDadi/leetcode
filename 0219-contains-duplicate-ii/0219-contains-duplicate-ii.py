class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for r in range(len(nums)):
            if nums[r] not in hashmap:
                hashmap[nums[r]] = r
            else:
                idx = hashmap[nums[r]]
                if abs(r-idx)<=k:
                    return True
                hashmap[nums[r]] = r
        return False