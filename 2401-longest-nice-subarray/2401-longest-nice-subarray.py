class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        xor = 0
        n = len(nums)
        maxlen = 0
        l = 0
        r = 0
        while(r<n):
            while((nums[r] & xor)!=0):
                xor^=nums[l]
                l+=1
            xor|=nums[r]
            maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen