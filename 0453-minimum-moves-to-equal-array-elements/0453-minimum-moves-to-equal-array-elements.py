class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min1 = min(nums)
        n = len(nums)
        ans = 0
        for i in range(n):
            ans+=(nums[i] - min1)
        return ans