class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        mid = nums[n//2]
        for i in range(n):
            ans+=(abs(mid - nums[i]))
        return ans