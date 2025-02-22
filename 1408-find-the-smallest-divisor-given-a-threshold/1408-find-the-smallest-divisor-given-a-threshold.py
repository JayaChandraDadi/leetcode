class Solution(object):
    def sum1(self,nums,k):
        c = 0
        for i in range(len(nums)):
            c+=(nums[i]+k-1)//k
        return c
    def smallestDivisor(self, nums, threshold):
        low =1
        high = max(nums)
        while(low<=high):
            mid = (low+high)//2
            x = self.sum1(nums,mid)
            if x<=threshold:
                high = mid-1
            else:
                low = mid+1
        return low
        