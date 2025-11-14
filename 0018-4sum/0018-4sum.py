class Solution(object):
    def fourSum(self, nums, target):
       nums.sort()
       n = len(nums)
       ans = []
       for i in range(n):
        if i>0 and nums[i-1]==nums[i]:
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j-1]==nums[j]:
                continue
            k = j+1
            l = n-1
            while(k<l):
                sum1 = nums[i]+nums[j]+nums[k]+nums[l]
                if sum1==target:
                    ans.append([nums[i],nums[j],nums[k],nums[l]])
                    while(k<l and nums[k+1]==nums[k]):
                        k+=1
                    while(k<l and nums[l]==nums[l-1]):
                        l-=1
                    k+=1
                    l-=1
                elif sum1>target:
                    l-=1
                else:
                    k+=1
                    
       return ans
