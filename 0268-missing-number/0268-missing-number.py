class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sum1 = (n)*(n+1)//2
        return sum1-sum(nums)