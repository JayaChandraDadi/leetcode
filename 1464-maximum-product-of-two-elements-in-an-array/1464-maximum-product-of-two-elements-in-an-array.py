class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxproduct = float('-inf')
        nums.sort()
        n = len(nums)
        return (nums[n-1]-1)*(nums[n-2] - 1)