class Solution(object):
    def count(self,i,target,nums,dp):
        if target==0:
            return 1
        if i==0:
            if target%nums[i]==0:
                return 1
            else:
                return 0
        if dp[i][target]!=-1:
            return dp[i][target]
        nottake = self.count(i-1,target,nums,dp)
        take = 0
        if target>=nums[i]:
            take = self.count(i,target-nums[i],nums,dp)
        dp[i][target]= take+nottake
        return dp[i][target]
    def change(self, amount, nums):
        n = len(nums)
        prev = [0]*(amount+1)
        for i in range(amount+1):
            if i%nums[0]==0:
                prev[i] = 1
        prev[0] = 1
        for i in range(1,n):
            temp = [0]*(amount+1)
            temp[0] = 1
            for target in range(0,amount+1):
                nottake = prev[target]
                take = 0
                if target>=nums[i]:
                    take = temp[target-nums[i]]
                temp[target]= take+nottake
            prev = temp
        return prev[amount]


       
        