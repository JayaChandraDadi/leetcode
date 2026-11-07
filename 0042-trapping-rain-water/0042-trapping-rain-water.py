class Solution:
    def trap(self, nums: list[int]) -> int:
        i = 0
        n = len(nums)
        j = n - 1
        leftmax = float('-inf')
        rightmax = float('-inf')
        ans = 0
        while(i<=j):
            if nums[i]<=nums[j]:
                if leftmax>nums[i]:
                    ans+=(leftmax - nums[i])
                else:
                    leftmax = nums[i]
                i+=1
            else:
                if rightmax>nums[j]:
                    ans+=(rightmax - nums[j])
                else:
                    rightmax = nums[j]
                j-=1
        return ans