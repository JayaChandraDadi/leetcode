class Solution(object):
    def count(self,nums,i,target,dp):
        if i==0:
            if target%nums[0]==0:
                return (target/nums[0])
            else:
                return float('inf')
        if dp[i][target]!=-1:
            return dp[i][target]
        nottake = self.count(nums,i-1,target,dp)
        take = float('inf')
        if target>=nums[i]:
            take = 1+self.count(nums,i,target-nums[i],dp)
        dp[i][target] = min(take,nottake)
        return dp[i][target]
    def coinChange(self, coins,amount):
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        if self.count(coins,n-1,amount,dp)==float('inf'):
            return -1
        else:
            return self.count(coins,n-1,amount,dp)
        
        