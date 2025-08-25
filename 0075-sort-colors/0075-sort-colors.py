class Solution(object):
    def sortColors(self, nums):
        temp0 = []
        temp1 = []
        temp2 = []
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i]==0:
                temp0.append(0)
            elif nums[i]==1:
                temp1.append(1)
            else:
                temp2.append(2)
        for i in range(len(temp0)):
            ans.append(temp0[i])
        for j in range(len(temp1)):
            ans.append(temp1[j])
        for k in range(len(temp2)):
            ans.append(temp2[k])
        for i in range(n):
            nums[i] = ans[i]
       
