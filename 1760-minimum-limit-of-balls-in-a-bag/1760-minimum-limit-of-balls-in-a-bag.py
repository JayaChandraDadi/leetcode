class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        n = len(nums)
        low = 1
        high = max(nums)
        ans = 0
        def operations(nums,mid):
            bags = 0
            for x in nums:
                bags+=((x-1)//mid)
            return bags
        while(low<=high):
            mid = (low + high)//2
            ops = operations(nums,mid)
            if ops<=maxOperations:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans