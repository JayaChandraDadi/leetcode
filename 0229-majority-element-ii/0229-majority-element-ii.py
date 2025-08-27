class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        ct1 = 0
        ct2 = 0
        el1 = 0
        el2 = 0
        for i in range(len(nums)):
            if ct1==0 and nums[i]!=el2:
                el1 = nums[i]
                ct1 = 1
            elif ct2==0 and nums[i]!=el1:
                el2 = nums[i]
                ct2 = 1
            elif nums[i]==el1:
                ct1+=1
            elif nums[i]==el2:
                ct2+=1
            else:
                ct1-=1
                ct2-=1
        ct1 = 0
        ct2 = 0
        ans = []
        for i in range(n):
            if nums[i]==el1:
                ct1+=1
            if nums[i]==el2:
                ct2+=1
        if ct1>(n//3):
            ans.append(el1)
        if ct2>(n//3) and el2!=el1:
            ans.append(el2)
        return ans
            
        