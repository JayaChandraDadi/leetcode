class Solution:
    def trap(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        leftmax = float('-inf')
        rightmax = float('-inf')
        ans = 0
        while(i<j):
            if nums[i]<=nums[j]:
                if leftmax<=nums[i]:
                    leftmax = nums[i]
                else:
                    ans+=(leftmax-nums[i])
                i+=1
            else:
                if rightmax<=nums[j]:
                    rightmax = nums[j]
                else:
                    ans+=(rightmax-nums[j])
                j-=1
        return ans