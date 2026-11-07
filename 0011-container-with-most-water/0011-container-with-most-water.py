class Solution:
    def maxArea(self, nums: list[int]) -> int:
        i = 0
        n = len(nums)
        j = n - 1
        ans = float('-inf')
        while(i<=j):
            if nums[i]<=nums[j]:
                ans = max(ans,nums[i]*(j-i))
                i+=1
            else:
                ans = max(ans,nums[j]*(j-i))
                j-=1
        return ans