class Solution(object):
    def subset(self,nums,target,i,dp):
        if target==0:
            return True
        if i==0:
            return (nums[0]==target)
        if dp[i][target]!=None:
            return dp[i][target]
        nottake = self.subset(nums,target,i-1,dp)
        take = False
        if target>=nums[i]:
            take = self.subset(nums,target-nums[i],i-1,dp)
        dp[i][target] = (nottake or take)
        return dp[i][target]
    def canPartition(self, nums):
        sum1 = sum(nums)
        if sum1%2==1:
            return False
        n = len(nums)
        target=sum1//2
        prev = [False]*(target+1) 
        prev[0] = True
        if target>=nums[0]:
            prev[nums[0]] = True
        for i in range(1,n):
            temp = [False]*(target+1)
            temp[0] = True
            for j in range(1,target+1):
                nottake = prev[j]
                take = False
                if j>=nums[i]:
                    take = prev[j-nums[i]]
                temp[j] = (nottake or take)
            prev = temp
        return prev[target]