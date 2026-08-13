class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ct = 0
        n = len(nums)
        if n<3:
            return 0
        l = 0
        r = 2
        while(r<n):
            diff1 = nums[r] - nums[r-1]
            diff2 = nums[r-1] - nums[r-2]
            if diff1==diff2:
                ct+=(r-l-1)
            else:
                l = r-1
            r+=1
        return ct