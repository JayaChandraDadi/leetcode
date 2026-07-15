class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        sum1 = 0
        minlen = float('inf')
        while(r<len(nums)):
            sum1+=nums[r]
            while(sum1>=target):
                minlen = min(minlen,r-l+1)
                sum1-=nums[l]
                l+=1
            r+=1
        return minlen if minlen!=float('inf') else 0