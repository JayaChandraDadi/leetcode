class Solution(object):
    def split(self,max1,nums):
        n = 1
        maxsum = 0
        for i in range(len(nums)):
            if maxsum+nums[i]<=max1:
                maxsum+=nums[i]
            else:
                n+=1
                maxsum = nums[i]
        return n
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        while(low<=high):
            mid = (low+high)//2
            x = self.split(mid,nums)
            if x<=k:
                high = mid-1
            else:
                low = mid+1
        return low

        