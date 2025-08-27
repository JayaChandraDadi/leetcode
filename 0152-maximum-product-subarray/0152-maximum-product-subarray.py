class Solution(object):
    def maxProduct(self, nums):
        pre =1
        suff = 1
        maxi = float('-inf')
        n = len(nums)
        for i in range(len(nums)):
            if pre==0:
                pre = 1
            if suff ==0:
                suff = 1
            pre = pre*(nums[i])
            suff = suff*(nums[n-i-1])
            maxi = max(maxi,pre,suff)
        return maxi

        
