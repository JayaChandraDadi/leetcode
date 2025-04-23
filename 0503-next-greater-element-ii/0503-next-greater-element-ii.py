class Solution(object):
    def nextGreaterElements(self, nums):
        ans = []
        n = len(nums)
        for i in range(len(nums)):
            found = False
            for j in range(i+1,i+len(nums)):
                ind = j%n
                if nums[ind]>nums[i]:
                    ans.append(nums[ind])
                    found = True
                    break
            if found==False:
                ans.append(-1)
        return ans

        