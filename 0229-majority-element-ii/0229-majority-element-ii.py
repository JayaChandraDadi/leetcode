class Solution(object):
    def majorityElement(self, nums):
        ct1 = 0
        ct2 = 0
        el1 = float('-inf')
        el2 = float('-inf')
        for i in range(len(nums)):
            if ct1==0 and nums[i]!=el2:
                ct1+=1
                el1 = nums[i]
            elif ct2==0 and nums[i]!=el1:
                ct2+=1
                el2 = nums[i]
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
        min1 = (len(nums)//3)+1
        for i in range(len(nums)):
            if nums[i]==el1:
                ct1+=1
            if nums[i]==el2:
                ct2+=1
        if ct1>=min1:
            ans.append(el1)
        if ct2>=min1:
            ans.append(el2)
        return ans

            
