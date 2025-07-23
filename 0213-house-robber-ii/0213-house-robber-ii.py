class Solution(object):
    def sum1(self,nums,n):
        prev1 = nums[0]
        prev2 = 0
        for i in range(1,n):
            if i-2>=0:
                take = nums[i] + prev2
            else:
                take = nums[i]
            nottake = prev1
            curri = max(take,nottake)
            prev2 = prev1
            prev1 = curri
        return prev1
    def rob(self, nums):
        n = len(nums)
        temp1 = []
        temp2 = []
        if n==1:
            return nums[0]
        for i in range(n):
            if i!=0:
                temp2.append(nums[i])
            if i!=n-1:
                temp1.append(nums[i])
        return max(self.sum1(temp1,len(temp1)),self.sum1(temp2,len(temp2)))
            

        
        