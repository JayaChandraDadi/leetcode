class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n = len(nums)
        min1 = float('inf')
        max1 = float('-inf')
        for i in range(n):
            min1 = min(min1,nums[i])
            max1 = max(max1,nums[i])
        if min1==max1 or max1%min1==0:
            return min1
        gcd = 1
        for i in range(2,min1+1):
            if max1%i==0 and min1%i==0:
                gcd = i
        return gcd