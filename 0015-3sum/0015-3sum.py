class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
               continue
            j = i+1
            k = n - 1
            while(j<k):
                sum1 = nums[i] + nums[j] + nums[k]
                if sum1==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1
                elif sum1>0:
                    k-=1
                else:
                    j+=1
        return ans
        #[-4,-1,-1,0,1,2]