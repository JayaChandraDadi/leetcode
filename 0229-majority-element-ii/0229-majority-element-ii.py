class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        ct1 = 0
        ct2 = 0
        el1 = 0
        el2 = 0
        n = len(nums)
        for i in range(n):
            if nums[i]==el1:
                ct1+=1
            elif nums[i]==el2:
                ct2+=1
            elif ct1==0:
                ct1 = 1
                el1 = nums[i]
            elif ct2==0:
                ct2 = 1
                el2 = nums[i]
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
        if ct2>(n//3):
            ans.append(el2)
        if el1==el2:
            ans.pop()
        return ans