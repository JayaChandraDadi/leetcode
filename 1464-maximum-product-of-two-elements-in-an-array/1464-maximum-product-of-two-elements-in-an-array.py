class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxproduct = float('-inf')
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                maxproduct = max(maxproduct,(nums[i]-1)*(nums[j]-1))
        return maxproduct